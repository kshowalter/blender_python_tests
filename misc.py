import bpy

def clear_objects():
    if bpy.context.mode != "OBJECT":
        bpy.ops.object.mode_set(mode='OBJECT')

    for item in bpy.data.objects:
        if item.type == "MESH":
            item.select = True
            bpy.ops.object.delete()
