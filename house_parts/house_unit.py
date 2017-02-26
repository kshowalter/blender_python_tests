import bpy
import imp

import csg
imp.reload(csg)

import misc
imp.reload(misc)

import mk_cube
imp.reload(mk_cube)
from mk_cube import mk_cube

import standard
imp.reload(standard)
from standard import standard


def build(location, specs):

    offset = {
        'x': specs['building_depth']/2-(specs['wall_thickness']/2),
        'y': specs['building_width']/2-(specs['wall_thickness']/2)
    }




    floor = mk_cube( (specs['building_depth'], specs['building_width'], specs['floor_thickness']), (0, 0,  specs['floor_thickness']/2) )


    wall_section_1 = mk_cube( (specs['building_depth'], specs['wall_thickness'], specs['wall_height']), (0, offset['y'],  specs['wall_height']/2) )
    wall_section_2 = mk_cube( (specs['wall_thickness'], specs['building_width'], specs['wall_height']), (offset['x'], 0,  specs['wall_height']/2) )
    wall_section_3 = mk_cube( (specs['building_depth'], specs['wall_thickness'], specs['wall_height']), (0, -offset['y'], specs['wall_height']/2) )
    wall_section_4 = mk_cube( (specs['wall_thickness'], specs['building_width'], specs['wall_height']), (-offset['x'], 0, specs['wall_height']/2) )

    csg.union( floor, wall_section_1 )
    csg.union( floor, wall_section_2 )
    csg.union( floor, wall_section_3 )
    csg.union( floor, wall_section_4 )

    frame = floor

    door1 = mk_cube( (specs['wall_thickness'], standard['door_width'], standard['door_height']), (offset['x'], 0,  standard['door_height']/2 + specs['floor_thickness'] ) )

    csg.difference( frame, door1 )

    porch_center = ( specs['building_depth']/2+specs['front_porch_depth']/2, 0,  specs['floor_thickness']/2)
    porch_floor = mk_cube( (specs['front_porch_depth'], specs['building_width'], specs['floor_thickness']), porch_center )

    posts = []
    post_location = [
        specs['building_depth']/2+specs['front_porch_depth']-specs['porch_post_diam']/2,
        -specs['building_width']/2+specs['porch_post_diam']/2,
        specs['wall_height']/2+specs['floor_thickness']/2
    ]
    for x in range(4):
        porch_post = mk_cube( (specs['porch_post_diam'], specs['porch_post_diam'], specs['wall_height']-specs['floor_thickness']), post_location )
        posts.append(porch_post)
        post_location[1] += (specs['building_width']-specs['porch_post_diam'])/3


    #g_house_unit = bpy.ops.group.create()
    bpy.ops.object.select_all(action='DESELECT')
    #print(bpy.context.selected_objects)
    for obj in posts:
        obj.select = True
    frame.select = True
    porch_floor.select = True
    #g_house_unit.add(bpy.context.active_object)
    bpy.ops.transform.translate(value=location)


    bpy.ops.object.select_all(action='DESELECT')
