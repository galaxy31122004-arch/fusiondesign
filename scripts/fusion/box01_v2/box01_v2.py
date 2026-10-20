"""Create a provisional box with parameter-driven corner fillets."""

import os
import traceback

import adsk.core
import adsk.fusion


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..',
                                            'projects', 'Box HybridLora'))
OUTPUT = os.path.join(PROJECT_ROOT, 'design', 'box01_v2.f3d')
BODY_MESH = os.path.join(PROJECT_ROOT, 'print', 'mesh', 'box01_body_v2.3mf')
LID_MESH = os.path.join(PROJECT_ROOT, 'print', 'mesh', 'box01_lid_v2.3mf')
REPORT = os.path.join(PROJECT_ROOT, 'runs', 'fusion_v2_run.txt')


def rectangle(sketch, length_expression, width_expression):
    lines = sketch.sketchCurves.sketchLines.addTwoPointRectangle(
        adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(12, 12, 0)
    )
    horizontal = None
    vertical = None
    for line in lines:
        a = line.startSketchPoint.geometry
        b = line.endSketchPoint.geometry
        if abs(a.y - b.y) < 0.001:
            horizontal = line
        elif abs(a.x - b.x) < 0.001:
            vertical = line
    if not horizontal or not vertical:
        raise RuntimeError('Could not identify rectangle edges')
    dims = sketch.sketchDimensions
    xdim = dims.addDistanceDimension(
        horizontal.startSketchPoint, horizontal.endSketchPoint,
        adsk.fusion.DimensionOrientations.HorizontalDimensionOrientation,
        adsk.core.Point3D.create(6, -1, 0)
    )
    ydim = dims.addDistanceDimension(
        vertical.startSketchPoint, vertical.endSketchPoint,
        adsk.fusion.DimensionOrientations.VerticalDimensionOrientation,
        adsk.core.Point3D.create(-1, 6, 0)
    )
    xdim.parameter.expression = length_expression
    ydim.parameter.expression = width_expression
    return sketch.profiles.item(0)


def add_parameter(design, name, value, comment):
    return design.userParameters.add(
        name, adsk.core.ValueInput.createByString(value), 'mm', comment
    )


def create_component(root, name, z_mm=0):
    transform = adsk.core.Matrix3D.create()
    if z_mm:
        transform.translation = adsk.core.Vector3D.create(0, 0, z_mm / 10)
    occurrence = root.occurrences.addNewComponent(transform)
    component = occurrence.component
    component.name = name
    return component


def round_vertical_corners(component, source_body, expected_height_mm):
    edges = adsk.core.ObjectCollection.create()
    for edge in source_body.edges:
        box = edge.boundingBox
        a, b = box.minPoint, box.maxPoint
        if (abs(a.x - b.x) < 0.001 and abs(a.y - b.y) < 0.001
                and abs((b.z - a.z) * 10 - expected_height_mm) < 0.01):
            edges.add(edge)
    if edges.count != 4:
        raise RuntimeError('Expected four vertical outside edges, found ' + str(edges.count))
    fillets = component.features.filletFeatures
    feature_input = fillets.createInput()
    feature_input.edgeSetInputs.addConstantRadiusEdgeSet(
        edges, adsk.core.ValueInput.createByString('corner_radius'), False
    )
    feature = fillets.add(feature_input)
    if not feature:
        raise RuntimeError('Outside corner fillet failed')
    feature.name = 'Four outside corner fillets'
    return feature.bodies.item(0)


def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface
    try:
        existing = [path for path in (OUTPUT, BODY_MESH, LID_MESH) if os.path.exists(path)]
        if existing:
            raise RuntimeError('Prototype exports already exist; no files were overwritten: '
                               + ', '.join(existing))
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        doc.name = 'box01_v2 - rounded prototype'
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            raise RuntimeError('Fusion design workspace is unavailable')
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType
        root = design.rootComponent

        # These are layout assumptions for the first model, not validated fits.
        add_parameter(design, 'box_length', '120 mm', 'Temporary outside length')
        add_parameter(design, 'box_width', '120 mm', 'Temporary outside width')
        add_parameter(design, 'body_height', '65 mm', 'Temporary body height')
        add_parameter(design, 'lid_thickness', '5 mm', 'Temporary lid thickness')
        add_parameter(design, 'wall_thickness', '3 mm', 'Temporary wall and bottom thickness')
        add_parameter(design, 'corner_radius', '4 mm', 'Temporary outside corner radius')
        add_parameter(design, 'pcb_length_ref', '100 mm', 'PCB reference only; mounting is pending')
        add_parameter(design, 'pcb_width_ref', '100 mm', 'PCB reference only; mounting is pending')

        body = create_component(root, '01 Body - open top, no ports')
        body_sketch = body.sketches.add(body.xYConstructionPlane)
        body_sketch.name = 'Outside footprint'
        body_profile = rectangle(body_sketch, 'box_length', 'box_width')
        body_extrudes = body.features.extrudeFeatures
        body_input = body_extrudes.createInput(
            body_profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )
        body_input.setDistanceExtent(False, adsk.core.ValueInput.createByString('body_height'))
        body_extrude = body_extrudes.add(body_input)
        body_extrude.name = 'Body outside'
        rounded_body = round_vertical_corners(body, body_extrude.bodies.item(0), 65)

        top = None
        top_z = -1e9
        for face in rounded_body.faces:
            point = face.pointOnFace
            if point.z > top_z:
                top = face
                top_z = point.z
        faces = adsk.core.ObjectCollection.create()
        faces.add(top)
        shell_input = body.features.shellFeatures.createInput(faces)
        shell_input.insideThickness = adsk.core.ValueInput.createByString('wall_thickness')
        shell = body.features.shellFeatures.add(shell_input)
        shell.name = 'Open body - wall and bottom'
        shell.bodies.item(0).name = 'Body prototype'

        lid = create_component(root, '02 Lid - flat placeholder', 65)
        lid_sketch = lid.sketches.add(lid.xYConstructionPlane)
        lid_sketch.name = 'Lid footprint'
        lid_profile = rectangle(lid_sketch, 'box_length', 'box_width')
        lid_input = lid.features.extrudeFeatures.createInput(
            lid_profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )
        lid_input.setDistanceExtent(False, adsk.core.ValueInput.createByString('lid_thickness'))
        lid_extrude = lid.features.extrudeFeatures.add(lid_input)
        lid_extrude.name = 'Flat lid placeholder'
        rounded_lid = round_vertical_corners(lid, lid_extrude.bodies.item(0), 5)
        rounded_lid.name = 'Lid prototype - no seal'

        export = design.exportManager
        options = export.createFusionArchiveExportOptions(OUTPUT)
        if not export.execute(options):
            raise RuntimeError('Fusion archive export failed')
        for component, filename in ((body, BODY_MESH), (lid, LID_MESH)):
            mesh_options = export.createC3MFExportOptions(component, filename)
            mesh_options.sendToPrintUtility = False
            if not export.execute(mesh_options):
                raise RuntimeError('3MF export failed: ' + filename)
        app.activeViewport.fit()
        with open(REPORT, 'w', encoding='utf-8') as result:
            result.write('Created: ' + OUTPUT + '\n')
            result.write('Created: ' + BODY_MESH + '\n')
            result.write('Created: ' + LID_MESH + '\n')
            result.write('Body 120 x 120 x 65 mm; lid 120 x 120 x 5 mm; wall/bottom 3 mm; corner radius 4 mm.\n')
            result.write('Prototype only: port and PCB hole dimensions pending; no gasket, chosen material, or water rating.\n')
        ui.messageBox('box01 v2 created and exported to:\n' + OUTPUT)
    except Exception:
        error = traceback.format_exc()
        with open(REPORT, 'w', encoding='utf-8') as result:
            result.write(error)
        ui.messageBox('box01 v2 script failed:\n' + error)
