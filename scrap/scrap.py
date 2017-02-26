def mk_cube_x(radius, location):
    bpy.ops.mesh.primitive_cube_add(radius = radius, location=location)
    cube = bpy.context.object
    #cube.delta_location += mathutils.Vector((1, 1, 1))
    return cube




#cube.delta_location = mathutils.Vector((1, 1, 1))
#time.sleep(2)
#cube.delta_location += mathutils.Vector((1, 1, 1))


#cube1 = mk_cube(radius = 2, location=(0,0,0))
#cube2 = mk_cube(radius = 1, location=(1,1,1))
#
#csgSubtract(cube1, cube2)
#
#bpy.ops.object.select_all(action='DESELECT')
#cube2.select = True
#bpy.ops.object.delete()


for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        override = bpy.context.copy()
        override['area'] = area
        clear_objects()
        build()
        break
