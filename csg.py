import bpy

def modifier(operation, target, opObj):
    '''subtract opObj from the target'''

    # Deselect All
    if bpy.context.mode != "OBJECT":
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    # Select the new object.
    target.select = True
    bpy.context.scene.objects.active = target

    # Add a modifier
    bpy.ops.object.modifier_add(type='BOOLEAN')

    mod = target.modifiers
    mod[0].name = "SubEmUp"
    mod[0].object = opObj
    mod[0].operation = operation

    # Apply modifier
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod[0].name)

    # Deselect All
    bpy.ops.object.select_all(action='DESELECT')

    # remove reference object
    opObj.select = True
    bpy.ops.object.delete()

    #recenter
    target.select = True
    if bpy.context.mode != "EDIT":
        bpy.ops.object.mode_set(mode='EDIT')
    old_type = bpy.context.area.type
    bpy.context.area.type = 'VIEW_3D'
    bpy.ops.mesh.select_all(action='SELECT')
    #bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.view3d.snap_cursor_to_center()
    bpy.context.area.type = old_type
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    #bpy.ops.object.origin_set(  )
    bpy.ops.object.select_all(action='DESELECT')

def difference(target, opObj):
    modifier('DIFFERENCE', target, opObj)

def union(target, opObj):
    modifier('UNION', target, opObj)

def intersect(target, opObj):
    modifier('INTERSECT', target, opObj)
