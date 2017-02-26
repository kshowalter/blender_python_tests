import os
import sys
import bpy
import imp

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

if bpy.context.mode != "OBJECT":
    bpy.ops.object.mode_set(mode='OBJECT')

# Create Left and Right vertex groups
center = ob.vertex_groups.new('center')
outer = ob.vertex_groups.new('outer')
roof = ob.vertex_groups.new('roof')
top = ob.vertex_groups.new('top')

for v in ob.data.vertices:
    if v.co[1] < 0.1 and v.co[1] > -0.1 and v.co[2] > 0.1:
        roof.add([v.index], 1.0, 'REPLACE')

    if v.co[1] < 0.1 and v.co[1] > -0.1:
        center.add([v.index], 1.0, 'REPLACE')
    else:
        outer.add([v.index], 1.0, 'REPLACE')

    if v.co[2] > 0.1:
        top .add([v.index], 1.0, 'REPLACE')

if bpy.context.mode != "EDIT":
    bpy.ops.object.mode_set(mode='EDIT')

bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_set_active(group='roof')
bpy.ops.object.vertex_group_select()
bpy.ops.transform.translate(value=(0, 0, 0.42), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
