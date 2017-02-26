import bpy
import imp

import csg
imp.reload(csg)

import misc
imp.reload(misc)

import mk_cube
imp.reload(mk_cube)
mk_cube = mk_cube.mk_cube

def build(location, specs):

    roof_overhang = specs['building_depth'] * 0.1
    roof_thickness = specs['wall_thickness']
    roof_width = specs['building_width']
    roof_depth = specs['building_depth'] + specs['front_porch_depth']

    roof = mk_cube( (roof_depth, roof_width, roof_thickness), (0, 0,  roof_thickness/2) )

    roof.select = True
    bpy.ops.transform.translate(value=( specs[ 'front_porch_depth']/2, 0, 0 ) )
    bpy.ops.transform.translate(value=location)

    bpy.ops.object.select_all(action='DESELECT')
