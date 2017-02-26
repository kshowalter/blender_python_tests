import os
import sys
import bpy
import imp
import bmesh

print('/---\\')

blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

import misc
imp.reload(misc)

misc.clear_objects()

bpy.ops.mesh.primitive_cube_add(radius=1, location=(0,0,0))
ob = bpy.context.object
ob.name = 'TestObj'
ob.show_name = True

if bpy.context.mode != "EDIT":
    bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.subdivide(number_cuts=1)

ob.update_from_editmode()

bpy.ops.mesh.select_all(action='DESELECT')
mesh = bmesh.from_edit_mesh(ob.data)

for v in mesh.verts:
    #print( v.co, v.co[1], v.co[1] < 0.1 , v.co[1] > -0.1 , v.co[2] > 0.1  )
    if v.co[1] < 0.1 and v.co[1] > -0.1 and v.co[2] > 0.1:
        #print( 'roof', v.index, v.co, v.co[2] )
        v.co[2] += 0.42

        

#ob.update_from_editmode()
#bpy.context.scene.objects.active = bpy.context.scene.objects.active