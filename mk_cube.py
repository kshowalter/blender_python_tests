#from create_mesh import *
import bpy
import imp

import create_mesh
imp.reload(create_mesh)
create_mesh = create_mesh.create_mesh

def mk_cube(size, location):
    origin = (0,0,0)
    (dx,dy,dz) = ( size[0]/2, size[1]/2, size[2]/2 )
    verts1 = (
        (dx,dy,dz),
        (dx,-dy,dz),
        (dx,-dy,-dz),
        (dx,dy,-dz),
        (-dx,-dy,dz),
        (-dx,dy,dz),
        (-dx,dy,-dz),
        (-dx,-dy,-dz),
    )
    faces1 = (
        (0,1,2,3),
        (4,5,6,7),
        (3,2,7,6),
        (2,1,4,7),
        (0,3,6,5),
        (1,0,5,4)
    )
    ob1 = create_mesh('Solid', location, verts1, [], faces1)

    return ob1
