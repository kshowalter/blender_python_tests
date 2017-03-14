import bpy

def clear_objects():
    if bpy.context.mode != "OBJECT":
        bpy.ops.object.mode_set(mode='OBJECT')

    for item in bpy.data.objects:
        if item.type == "MESH":
            item.select = True
            bpy.ops.object.delete()


def clear_obj_materials():
    obj = bpy.context.active_object
    mesh = obj.data
    while len(mesh.materials)>1:
        mesh.materials.pop()



def clear_all_materials():
    for material in bpy.data.materials:
        material.user_clear();
        bpy.data.materials.remove(material);
