"""Create a rounded prototype enclosure with four blind PCB mounting bosses."""

import os
import traceback
from datetime import datetime

import adsk.core
import adsk.fusion


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..',
                                            'projects', 'box-hybrid-lora'))
OUTPUT = os.path.join(PROJECT_ROOT, 'design', 'box-hybrid-lora_v03.f3d')
BODY_MESH = os.path.join(PROJECT_ROOT, 'print', 'mesh', 'box-hybrid-lora_v03_body.3mf')
LID_MESH = os.path.join(PROJECT_ROOT, 'print', 'mesh', 'box-hybrid-lora_v03_lid.3mf')
REPORT = os.path.join(PROJECT_ROOT, 'runs', 'fusion_v3_run.txt')


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


def add_pcb_mounting_bosses(body):
    # Board origin is provisionally (10, 10) mm. The horizontal inset mirrors
    # the measured lower-edge inset; only the vertical spacing was dimensioned.
    board_origin_mm = 10.0
    inset_mm = 2.436
    far_y_mm = inset_mm + 94.679
    positions_mm = (
        (board_origin_mm + inset_mm, board_origin_mm + inset_mm),
        (board_origin_mm + 100 - inset_mm, board_origin_mm + inset_mm),
        (board_origin_mm + inset_mm, board_origin_mm + far_y_mm),
        (board_origin_mm + 100 - inset_mm, board_origin_mm + far_y_mm),
    )
    for index, (x_mm, y_mm) in enumerate(positions_mm, start=1):
        sketch = body.sketches.add(body.xYConstructionPlane)
        sketch.name = 'Mount %d footprint - provisional X' % index
        circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(
            adsk.core.Point3D.create(x_mm / 10, y_mm / 10, 0), 0.25
        )
        diameter = sketch.sketchDimensions.addDiameterDimension(
            circle, adsk.core.Point3D.create(x_mm / 10 + 0.5, y_mm / 10, 0)
        )
        diameter.parameter.expression = 'boss_diameter'
        boss_input = body.features.extrudeFeatures.createInput(
            sketch.profiles.item(0), adsk.fusion.FeatureOperations.JoinFeatureOperation
        )
        boss_input.setDistanceExtent(False, adsk.core.ValueInput.createByString('wall_thickness + pcb_standoff_height'))
        boss = body.features.extrudeFeatures.add(boss_input)
        boss.name = 'PCB boss %d - outside diameter 5 mm' % index

    top_plane_input = body.constructionPlanes.createInput()
    if not top_plane_input.setByOffset(
            body.xYConstructionPlane,
            adsk.core.ValueInput.createByString('wall_thickness + pcb_standoff_height')):
        raise RuntimeError('Could not create mounting-hole plane')
    top_plane = body.constructionPlanes.add(top_plane_input)
    top_plane.name = 'PCB boss tops'
    for index, (x_mm, y_mm) in enumerate(positions_mm, start=1):
        sketch = body.sketches.add(top_plane)
        sketch.name = 'Mount %d blind hole' % index
        circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(
            adsk.core.Point3D.create(x_mm / 10, y_mm / 10, 0), 0.1
        )
        diameter = sketch.sketchDimensions.addDiameterDimension(
            circle, adsk.core.Point3D.create(x_mm / 10 + 0.3, y_mm / 10, 0)
        )
        diameter.parameter.expression = 'mount_hole_diameter'
        cut_input = body.features.extrudeFeatures.createInput(
            sketch.profiles.item(0), adsk.fusion.FeatureOperations.CutFeatureOperation
        )
        cut_input.setDistanceExtent(False, adsk.core.ValueInput.createByString('-4 mm'))
        hole = body.features.extrudeFeatures.add(cut_input)
        hole.name = 'PCB hole %d - diameter 2 mm, blind' % index
    return positions_mm


def close_older_project_tabs(app, current_document):
    notes = []
    backup_dir = os.path.join(PROJECT_ROOT, 'runs', 'session_backups')
    for document in list(app.documents):
        if document == current_document:
            continue
        old_design = adsk.fusion.Design.cast(
            document.products.itemByProductType('DesignProductType')
        )
        if not old_design:
            continue
        root = old_design.rootComponent
        marker = root.attributes.itemByName('FusionDesign', 'project_id')
        is_project = marker and marker.value in ('box-hybrid-lora', 'box01')
        legacy_project = (document.name.startswith(('box01_v', 'box-hybrid-lora_v')) and
                        any(item.component.name.startswith('01 Body -')
                            for item in root.occurrences))
        if not is_project and not legacy_project:
            continue
        old_name = document.name
        try:
            if document.isModified:
                os.makedirs(backup_dir, exist_ok=True)
                stamp = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
                safe_name = ''.join(c if c.isalnum() or c in '-_' else '_'
                                    for c in document.name)
                backup = os.path.join(backup_dir, safe_name + '-' + stamp + '.f3d')
                archive = old_design.exportManager.createFusionArchiveExportOptions(backup)
                if not old_design.exportManager.execute(archive):
                    raise RuntimeError('Could not back up ' + old_name)
                notes.append('Backed up old tab: ' + backup)
            if not document.close(False):
                raise RuntimeError('Could not close ' + old_name)
            notes.append('Closed old tab: ' + old_name)
        except Exception as exc:
            notes.append('Kept old tab open: %s (%s)' % (old_name, exc))
    current_document.activate()
    return notes


def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface
    try:
        existing = [path for path in (OUTPUT, BODY_MESH, LID_MESH) if os.path.exists(path)]
        if existing:
            raise RuntimeError('Prototype exports already exist; no files were overwritten: '
                               + ', '.join(existing))
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        doc.name = 'box-hybrid-lora_v03 - PCB mounting prototype'
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            raise RuntimeError('Fusion design workspace is unavailable')
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType
        root = design.rootComponent
        root.attributes.add('FusionDesign', 'project_id', 'box-hybrid-lora')

        # These are layout assumptions for the first model, not validated fits.
        add_parameter(design, 'box_length', '120 mm', 'Temporary outside length')
        add_parameter(design, 'box_width', '120 mm', 'Temporary outside width')
        add_parameter(design, 'body_height', '65 mm', 'Temporary body height')
        add_parameter(design, 'lid_thickness', '5 mm', 'Temporary lid thickness')
        add_parameter(design, 'wall_thickness', '3 mm', 'Temporary wall and bottom thickness')
        add_parameter(design, 'corner_radius', '4 mm', 'Temporary outside corner radius')
        add_parameter(design, 'pcb_standoff_height', '5 mm', 'Temporary rise above the inner floor')
        add_parameter(design, 'boss_diameter', '5 mm', 'Temporary PCB support outside diameter')
        add_parameter(design, 'mount_hole_diameter', '2 mm', 'Blind hole matching PCB nominal diameter')
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
        mounting_positions = add_pcb_mounting_bosses(body)

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
            result.write('PCB boss centers, mm: ' + repr(mounting_positions) + '\n')
            result.write('Four 5 mm bosses with blind 2 mm holes; horizontal PCB hole inset assumed 2.436 mm.\n')
            result.write('Prototype only: no antenna/DC ports, gasket, chosen material, or water rating.\n')
            for note in close_older_project_tabs(app, doc):
                result.write(note + '\n')
        ui.messageBox('Box HybridLora v03 exported to:\n' + OUTPUT +
                      '\n\nPROTOTYPE ONLY: PCB X positions are assumed; antenna/DC ports, gasket, material and water protection are unfinished.')
    except Exception:
        error = traceback.format_exc()
        with open(REPORT, 'w', encoding='utf-8') as result:
            result.write(error)
        ui.messageBox('Box HybridLora v03 script failed:\n' + error)
