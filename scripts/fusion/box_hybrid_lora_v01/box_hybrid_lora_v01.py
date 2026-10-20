"""Create a provisional, parameter-driven enclosure in Autodesk Fusion."""

import os
import traceback

import adsk.core
import adsk.fusion


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..',
                                            'projects', 'box-hybrid-lora'))
OUTPUT = os.path.join(PROJECT_ROOT, 'design', 'box-hybrid-lora_v01.f3d')
BODY_MESH = os.path.join(PROJECT_ROOT, 'print', 'mesh', 'box-hybrid-lora_v01_body.3mf')
LID_MESH = os.path.join(PROJECT_ROOT, 'print', 'mesh', 'box-hybrid-lora_v01_lid.3mf')
REPORT = os.path.join(PROJECT_ROOT, 'runs', 'fusion_run.txt')


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


def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface
    try:
        existing = [path for path in (OUTPUT, BODY_MESH, LID_MESH) if os.path.exists(path)]
        if existing:
            raise RuntimeError('Prototype exports already exist; no files were overwritten: '
                               + ', '.join(existing))
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        doc.name = 'box-hybrid-lora_v01 - prototype'
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

        top = None
        top_z = -1e9
        for face in body_extrude.bodies.item(0).faces:
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
        lid_extrude.bodies.item(0).name = 'Lid prototype - no seal'

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
            result.write('Body 120 x 120 x 65 mm; lid 120 x 120 x 5 mm; wall/bottom 3 mm.\n')
            result.write('Prototype only: no PCB mounts, ports, gasket, chosen material, or water rating.\n')
        ui.messageBox('Box HybridLora v01 exported to:\n' + OUTPUT)
    except Exception:
        error = traceback.format_exc()
        with open(REPORT, 'w', encoding='utf-8') as result:
            result.write(error)
        ui.messageBox('Box HybridLora v01 script failed:\n' + error)
