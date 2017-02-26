import bpy
import imp
import time
import mathutils

#from mk_cube import *
import mk_cube
imp.reload(mk_cube)
from mk_cube import mk_cube

import csg
imp.reload(csg)

import misc
imp.reload(misc)

import house_parts
imp.reload(house_parts)
from house_parts import house_unit, roof
imp.reload(house_unit)
imp.reload(roof)



def build(location, specs):

    house_unit_1 = house_unit.build(location, specs)
    location[2] += specs['wall_height']
    house_unit_2 = house_unit.build(location, specs)
    location[2] += specs['wall_height']
    roof_1 = roof.build(location, specs)


    #return house_unit_1
