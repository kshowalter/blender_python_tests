import bpy

def mk_material():

    if bpy.context.mode != "OBJECT":
        bpy.ops.object.mode_set(mode='OBJECT')





    material = bpy.data.materials.new(name='concrete')


    #bpy.context.object.active_material.name = 'concrete'
    material.diffuse_color = ( 0.8, 0.8, 0.8 )
    material.diffuse_shader = 'LAMBERT'
    material.diffuse_intensity = 0.8
    material.specular_color = ( 0.8, 0.8, 0.8 )
    material.specular_shader = 'COOKTORR'
    material.specular_intensity = 0.2
    material.specular_hardness = 10

    texture = bpy.ops.texture.new()
    #material.texture_slots.append(texture)
    texture = bpy.data.textures['Texture']
    texture.name = 'concrete'
    texture.type = 'MUSGRAVE'
    texture.musgrave_type = 'MULTIFRACTAL'
    texture.scale[0] = 100
    texture.scale[1] = 100
    texture.scale[2] = 100

def add_material(obj, material):

    ob.data.materials.append(material)



if __name__ == "__main__":
    obj = bpy.context.active_object
    
    # clear existing material
    ob_mat = obj.data.materials.get('concrete')
    if( ob_mat ):
        ob_mat.user_clear();
        ob.data.materials.remove(ob_mat)
        bpy.data.materials.remove(ob_mat)


    obj.data.materials.clear()

    mat = mk_material()

    add_material(obj, material)
