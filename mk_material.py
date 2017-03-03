import bpy

def mk_material():

    if bpy.context.mode != "OBJECT":
        bpy.ops.object.mode_set(mode='OBJECT')

    # Assign it to object
    ob = bpy.context.active_object
    ob.data.materials.clear()
    
    # clear existing material
    ob_mat = ob.data.materials.get('concrete')
    if( ob_mat ):
        ob_mat.user_clear();
        ob.data.materials.remove(ob_mat)
        bpy.data.materials.remove(ob_mat)
        
    mat = bpy.data.materials.new(name='concrete')
    ob.data.materials.append(mat)

    #bpy.context.object.active_material.name = 'concrete'
    bpy.context.object.active_material.diffuse_color = ( 0.8, 0.8, 0.8 )
    bpy.context.object.active_material.diffuse_shader = 'LAMBERT'
    bpy.context.object.active_material.diffuse_intensity = 0.8
    bpy.context.object.active_material.specular_color = ( 0.8, 0.8, 0.8 )
    bpy.context.object.active_material.specular_shader = 'COOKTORR'
    bpy.context.object.active_material.specular_intensity = 0.2
    bpy.context.object.active_material.specular_hardness = 10


    bpy.ops.texture.new()
    bpy.data.textures['Texture'].name = 'concrete'
    bpy.data.textures['concrete'].type = 'MUSGRAVE'
    bpy.data.textures['concrete'].musgrave_type = 'MULTIFRACTAL'


mk_material()
