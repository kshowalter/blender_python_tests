import bpy
import imp

import house
imp.reload(house)

def build():

    house_specs = {
        'wall_thickness':  0.2,
        'floor_thickness':  0.2,
        'wall_height': 4,
        'building_width': 5,
        'building_depth': 10,
        'front_porch_depth': 2,
        'porch_post_diam': 0.2
    }

    location = [ -15, house_specs['building_width'], 0]
    house.build(location, house_specs)
    location = [-15,0,0]
    house.build(location, house_specs)
    location = [ -15, -house_specs['building_width'], 0]
    house.build(location, house_specs)
