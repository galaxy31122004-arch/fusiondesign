"""Create the Box HybridLora v1.0.0 enclosure prototype."""

import os
import traceback
from datetime import datetime

import adsk.core
import adsk.fusion


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..',
                                            'projects', 'box-hybrid-lora'))
OUTPUT = os.path.join(PROJECT_ROOT, 'design', 'box-hybrid-lora_v1.0.0.f3d')
BODY_MESH = os.path.join(PROJECT_ROOT, 'runs', 'mesh', 'box-hybrid-lora_v1.0.0_body.3mf')
LID_MESH = os.path.join(PROJECT_ROOT, 'runs', 'mesh', 'box-hybrid-lora_v1.0.0_lid.3mf')
REPORT = os.path.join(PROJECT_ROOT, 'runs', 'fusion_v1.0.0_run.txt')


def rectangle(sketch, length_expression, width_expression):
    lines = sketch.sketchCurves.sketchLines.addTwoPointRectangle(
        adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(12, 12, 0)
    )
    origin_corner = min(
        (line.startSketchPoint for line in lines),
        key=lambda point: point.geometry.x * point.geometry.x
        + point.geometry.y * point.geometry.y
    )
    sketch.geometricConstraints.addCoincident(origin_corner, sketch.originPoint)
    horizontal = None
    vertical = None
    for line in lines:
        a = line.startSketchPoint.geometry
        b = line.endSketchPoint.geometry
        if abs(a.y - b.y) < 0.001 and a.x < b.x:
            horizontal = line
        elif abs(a.x - b.x) < 0.001 and a.y < b.y:
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


def check_xy_bounds(source_body, expected_length_mm, expected_width_mm, label):
    box = source_body.boundingBox
    actual = (box.minPoint.x, box.maxPoint.x, box.minPoint.y, box.maxPoint.y)
    expected = (0, expected_length_mm / 10, 0, expected_width_mm / 10)
    if any(abs(a - b) > 0.01 for a, b in zip(actual, expected)):
        raise RuntimeError('%s footprint shifted: actual cm=%s, expected cm=%s' %
                           (label, actual, expected))


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
    # Board origin is provisionally (23, 23) mm. The horizontal inset mirrors
    # the measured lower-edge inset; only the vertical spacing was dimensioned.
    board_origin_mm = 23.0
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
        circle.centerSketchPoint.isFixed = True
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
        circle.centerSketchPoint.isFixed = True
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


def offset_plane(component, offset_expression, name):
    plane_input = component.constructionPlanes.createInput()
    if not plane_input.setByOffset(
            component.xYConstructionPlane,
            adsk.core.ValueInput.createByString(offset_expression)):
        raise RuntimeError('Could not create plane: ' + name)
    plane = component.constructionPlanes.add(plane_input)
    plane.name = name
    return plane


def circle_profile(sketch, x_mm, y_mm, diameter_expression, initial_diameter_mm):
    circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(
        adsk.core.Point3D.create(x_mm / 10, y_mm / 10, 0),
        initial_diameter_mm / 20
    )
    circle.centerSketchPoint.isFixed = True
    dimension = sketch.sketchDimensions.addDiameterDimension(
        circle, adsk.core.Point3D.create((x_mm + initial_diameter_mm) / 10,
                                        y_mm / 10, 0)
    )
    dimension.parameter.expression = diameter_expression
    return sketch.profiles.item(0)


def extrude_profile(component, profile, operation, distance, name):
    features = component.features.extrudeFeatures
    feature_input = features.createInput(profile, operation)
    feature_input.setDistanceExtent(False, adsk.core.ValueInput.createByString(distance))
    feature = features.add(feature_input)
    if not feature:
        raise RuntimeError('Extrude failed: ' + name)
    feature.name = name
    return feature


def add_lid_screw_posts(body):
    positions = ((10.5, 10.5), (135.5, 10.5),
                 (10.5, 135.5), (135.5, 135.5))
    for index, (x_mm, y_mm) in enumerate(positions, 1):
        sketch = body.sketches.add(body.xYConstructionPlane)
        sketch.name = 'Lid screw post %d footprint' % index
        profile = circle_profile(sketch, x_mm, y_mm, 'lid_post_diameter', 9)
        extrude_profile(body, profile, adsk.fusion.FeatureOperations.JoinFeatureOperation,
                        'body_height', 'Lid screw post %d' % index)
    top_plane = offset_plane(body, 'body_height', 'Lid screw pilot plane')
    for index, (x_mm, y_mm) in enumerate(positions, 1):
        sketch = body.sketches.add(top_plane)
        sketch.name = 'Lid screw pilot %d' % index
        profile = circle_profile(sketch, x_mm, y_mm, 'lid_pilot_diameter', 2.5)
        extrude_profile(body, profile, adsk.fusion.FeatureOperations.CutFeatureOperation,
                        '-lid_pilot_depth', 'Lid screw blind pilot %d' % index)
    return positions


def add_mounting_ears(body):
    positions = ((-4.5, 28), (-4.5, 118),
                 (150.5, 28), (150.5, 118))
    for index, (x_mm, y_mm) in enumerate(positions, 1):
        sketch = body.sketches.add(body.xYConstructionPlane)
        sketch.name = 'Outer mounting ear %d' % index
        profile = circle_profile(sketch, x_mm, y_mm, 'ear_diameter', 14)
        extrude_profile(body, profile, adsk.fusion.FeatureOperations.JoinFeatureOperation,
                        'ear_thickness', 'Mounting ear %d' % index)
    top_plane = offset_plane(body, 'ear_thickness', 'Mounting ear hole plane')
    for index, (x_mm, y_mm) in enumerate(positions, 1):
        sketch = body.sketches.add(top_plane)
        sketch.name = 'Outer mounting hole %d' % index
        profile = circle_profile(sketch, x_mm, y_mm, 'ear_hole_diameter', 4.5)
        extrude_profile(body, profile, adsk.fusion.FeatureOperations.CutFeatureOperation,
                        '-ear_thickness', 'Ear through hole %d' % index)
    return positions


def add_inner_rim(body):
    plane = offset_plane(body, 'body_height - 4 mm', 'Inner rim base')
    sketch = body.sketches.add(plane)
    sketch.name = 'Rim supports screw posts and gasket channel'
    lines = sketch.sketchCurves.sketchLines
    lines.addTwoPointRectangle(adsk.core.Point3D.create(0.2, 0.2, 0),
                               adsk.core.Point3D.create(14.4, 14.4, 0))
    lines.addTwoPointRectangle(adsk.core.Point3D.create(2.0, 2.0, 0),
                               adsk.core.Point3D.create(12.6, 12.6, 0))
    rings = [profile for profile in sketch.profiles if profile.profileLoops.count == 2]
    if len(rings) != 1:
        raise RuntimeError('Expected one inner rim profile')
    extrude_profile(body, rings[0], adsk.fusion.FeatureOperations.JoinFeatureOperation,
                    '4 mm', 'Internal rim with 106 mm PCB insertion opening')


def add_gasket_groove(body):
    top_plane = offset_plane(body, 'body_height', 'Gasket groove plane')
    sketch = body.sketches.add(top_plane)
    sketch.name = 'Gasket channel - provisional 2 mm cord'
    lines = sketch.sketchCurves.sketchLines
    lines.addTwoPointRectangle(adsk.core.Point3D.create(1.62, 1.62, 0),
                               adsk.core.Point3D.create(12.98, 12.98, 0))
    lines.addTwoPointRectangle(adsk.core.Point3D.create(1.84, 1.84, 0),
                               adsk.core.Point3D.create(12.76, 12.76, 0))
    rings = [profile for profile in sketch.profiles if profile.profileLoops.count == 2]
    if len(rings) != 1:
        raise RuntimeError('Expected one closed gasket channel profile')
    extrude_profile(body, rings[0], adsk.fusion.FeatureOperations.CutFeatureOperation,
                    '-gasket_groove_depth', 'Continuous gasket groove in body rim')


def add_antenna_bulkhead_hole(body):
    plane_input = body.constructionPlanes.createInput()
    if not plane_input.setByOffset(
            body.yZConstructionPlane,
            adsk.core.ValueInput.createByString('box_length')):
        raise RuntimeError('Could not create right-side SMA plane')
    side_plane = body.constructionPlanes.add(plane_input)
    side_plane.name = 'SMA bulkhead plane on right wall'
    sketch = body.sketches.add(side_plane)
    sketch.name = 'SMA bulkhead at upper right - test opening'
    center = sketch.modelToSketchSpace(adsk.core.Point3D.create(14.6, 12.2, 5.5))
    circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(center, 0.33)
    dimension = sketch.sketchDimensions.addDiameterDimension(
        circle, adsk.core.Point3D.create(center.x + 0.6, center.y, 0)
    )
    dimension.parameter.expression = 'antenna_panel_hole'
    try:
        feature_input = body.features.extrudeFeatures.createInput(
            sketch.profiles.item(0), adsk.fusion.FeatureOperations.CutFeatureOperation
        )
        feature_input.setSymmetricExtent(
            adsk.core.ValueInput.createByString('2 * wall_thickness'), True
        )
        body.features.extrudeFeatures.add(feature_input).name = 'SMA bulkhead through wall - test fit'
    except Exception as exc:
        plane_origin = side_plane.geometry.origin
        plane_normal = side_plane.geometry.normal
        actual_center = sketch.sketchToModelSpace(center)
        bounds = []
        for item in body.bRepBodies:
            bbox = item.boundingBox
            bounds.append('%s:(%.2f..%.2f,%.2f..%.2f,%.2f..%.2f)' % (
                item.name, bbox.minPoint.x, bbox.maxPoint.x,
                bbox.minPoint.y, bbox.maxPoint.y, bbox.minPoint.z, bbox.maxPoint.z))
        raise RuntimeError(
            'SMA cut failed: plane x=%.3f normal x=%.3f, center=(%.3f, %.3f, %.3f), '
            'bodies=%s' % (
                plane_origin.x, plane_normal.x, actual_center.x, actual_center.y,
                actual_center.z, '; '.join(bounds))
        ) from exc


def fillet_lid_top_edges(lid, source_body):
    edges = adsk.core.ObjectCollection.create()
    for edge in source_body.edges:
        box = edge.boundingBox
        if abs(box.minPoint.z - 0.5) < 0.001 and abs(box.maxPoint.z - 0.5) < 0.001:
            edges.add(edge)
    if edges.count < 4:
        raise RuntimeError('Lid upper perimeter edges not found')
    feature_input = lid.features.filletFeatures.createInput()
    feature_input.edgeSetInputs.addConstantRadiusEdgeSet(
        edges, adsk.core.ValueInput.createByString('lid_top_radius'), False
    )
    feature = lid.features.filletFeatures.add(feature_input)
    if not feature:
        raise RuntimeError('Lid top edge fillet failed')
    feature.name = 'Soft rounded top edge of lid'


def add_lid_clearance_holes(lid, positions):
    top_plane = offset_plane(lid, 'lid_thickness', 'Lid fastener top plane')
    for index, (x_mm, y_mm) in enumerate(positions, 1):
        sketch = lid.sketches.add(top_plane)
        sketch.name = 'Lid clearance hole %d' % index
        profile = circle_profile(sketch, x_mm, y_mm, 'lid_clearance_diameter', 3.4)
        extrude_profile(lid, profile, adsk.fusion.FeatureOperations.CutFeatureOperation,
                        '-lid_thickness', 'Lid screw through hole %d' % index)
        recess = lid.sketches.add(top_plane)
        recess.name = 'Lid screw head recess %d' % index
        profile = circle_profile(recess, x_mm, y_mm, 'lid_head_recess_diameter', 6.5)
        extrude_profile(lid, profile, adsk.fusion.FeatureOperations.CutFeatureOperation,
                        '-lid_head_recess_depth', 'Lid screw head recess %d' % index)


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
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    try:
        existing = [path for path in (OUTPUT, BODY_MESH, LID_MESH) if os.path.exists(path)]
        if existing:
            raise RuntimeError('Prototype exports already exist; no files were overwritten: '
                               + ', '.join(existing))
        os.makedirs(os.path.dirname(BODY_MESH), exist_ok=True)
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        doc.name = 'box-hybrid-lora_v1.0.0 - antenna and seal prototype'
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            raise RuntimeError('Fusion design workspace is unavailable')
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType
        root = design.rootComponent
        root.attributes.add('FusionDesign', 'project_id', 'box-hybrid-lora')

        # These are layout assumptions for the first model, not validated fits.
        add_parameter(design, 'box_length', '146 mm', 'Temporary outside length')
        add_parameter(design, 'box_width', '146 mm', 'Temporary outside width')
        add_parameter(design, 'body_height', '68 mm', 'Temporary body height')
        add_parameter(design, 'lid_thickness', '5 mm', 'Temporary lid thickness')
        add_parameter(design, 'wall_thickness', '5 mm', 'Temporary wall and bottom thickness')
        add_parameter(design, 'corner_radius', '4 mm', 'Temporary outside corner radius')
        add_parameter(design, 'lid_top_radius', '1.2 mm', 'Rounded top edge of lid')
        add_parameter(design, 'pcb_standoff_height', '5 mm', 'Temporary rise above the inner floor')
        add_parameter(design, 'boss_diameter', '5 mm', 'Temporary PCB support outside diameter')
        add_parameter(design, 'mount_hole_diameter', '2 mm', 'Blind hole matching PCB nominal diameter')
        add_parameter(design, 'lid_post_diameter', '9 mm', 'Four independent lid screw posts')
        add_parameter(design, 'lid_pilot_diameter', '2.5 mm', 'Trial pilot for M3 fastener; test with actual screw')
        add_parameter(design, 'lid_pilot_depth', '12 mm', 'Blind lid screw engagement')
        add_parameter(design, 'lid_clearance_diameter', '3.4 mm', 'Trial lid screw clearance')
        add_parameter(design, 'lid_head_recess_diameter', '6.5 mm', 'Trial screw head recess')
        add_parameter(design, 'lid_head_recess_depth', '1.5 mm', 'Trial screw head recess depth')
        add_parameter(design, 'gasket_cord_diameter', '2 mm', 'Trial cord only; actual cord not selected')
        add_parameter(design, 'gasket_groove_width', '2.2 mm', 'Trial groove width; square path outside the PCB envelope')
        add_parameter(design, 'gasket_groove_depth', '1.5 mm', 'Trial groove depth')
        add_parameter(design, 'antenna_panel_hole', '6.6 mm', 'Trial SMA opening; measure actual connector')
        add_parameter(design, 'ear_diameter', '14 mm', 'Outside mounting ear diameter')
        add_parameter(design, 'ear_hole_diameter', '4.5 mm', 'Trial mounting screw clearance')
        add_parameter(design, 'ear_thickness', '5 mm', 'Mounting ear thickness')
        add_parameter(design, 'pcb_length_ref', '100 mm', 'PCB reference only; mounting is pending')
        add_parameter(design, 'pcb_width_ref', '100 mm', 'PCB reference only; mounting is pending')

        body = create_component(root, '01 Body - antenna, gasket groove and fasteners')
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
        check_xy_bounds(body_extrude.bodies.item(0), 146, 146, 'Body')
        rounded_body = round_vertical_corners(body, body_extrude.bodies.item(0), 68)

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
        shell.name = 'Open body - 5 mm walls and bottom'
        shell.bodies.item(0).name = 'Body with mounting features'
        add_inner_rim(body)
        add_gasket_groove(body)
        mounting_positions = add_pcb_mounting_bosses(body)
        lid_positions = add_lid_screw_posts(body)
        ear_positions = add_mounting_ears(body)
        if body.bRepBodies.count != 1:
            raise RuntimeError('Body has %d solids; mounting ears must join the shell' %
                               body.bRepBodies.count)
        add_antenna_bulkhead_hole(body)

        lid = create_component(root, '02 Lid - rounded top and four screw holes', 68)
        lid_sketch = lid.sketches.add(lid.xYConstructionPlane)
        lid_sketch.name = 'Lid footprint'
        lid_profile = rectangle(lid_sketch, 'box_length', 'box_width')
        lid_input = lid.features.extrudeFeatures.createInput(
            lid_profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )
        lid_input.setDistanceExtent(False, adsk.core.ValueInput.createByString('lid_thickness'))
        lid_extrude = lid.features.extrudeFeatures.add(lid_input)
        lid_extrude.name = 'Flat lid placeholder'
        check_xy_bounds(lid_extrude.bodies.item(0), 146, 146, 'Lid')
        rounded_lid = round_vertical_corners(lid, lid_extrude.bodies.item(0), 5)
        fillet_lid_top_edges(lid, rounded_lid)
        add_lid_clearance_holes(lid, lid_positions)
        lid.bRepBodies.item(0).name = 'Rounded screw lid - no gasket'

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
            result.write('Body 146 x 146 x 68 mm; lid 146 x 146 x 5 mm; wall/bottom 5 mm.\n')
            result.write('PCB boss centers, mm: ' + repr(mounting_positions) + '\n')
            result.write('Lid screw centers, mm: ' + repr(lid_positions) + '\n')
            result.write('Outer mounting ear centers, mm: ' + repr(ear_positions) + '\n')
            result.write('Trial gasket groove 2.2 mm wide x 1.5 mm deep on body only.\n')
            result.write('Trial SMA port diameter 6.6 mm at right wall Y=122 Z=55 mm.\n')
            result.write('Prototype only: gasket/SMA and PCB fit unverified; DC entry not designed; no water rating.\n')
            for note in close_older_project_tabs(app, doc):
                result.write(note + '\n')
        ui.messageBox('Box HybridLora v1.0.0 exported to:\n' + OUTPUT +
                      '\n\nPROTOTYPE ONLY: gasket and SMA openings need a physical fit test; DC entry and water protection are unfinished.')
    except Exception:
        error = traceback.format_exc()
        with open(REPORT, 'w', encoding='utf-8') as result:
            result.write(error)
        ui.messageBox('Box HybridLora v1.0.0 script failed:\n' + error)
