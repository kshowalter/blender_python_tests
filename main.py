import os
import sys
import bpy
import imp

blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

import neighbourhood
imp.reload(neighbourhood)

import misc
imp.reload(misc)

misc.clear_objects()

neighbourhood.build()
