import bpy
import numpy as np
from parametric_surfaces import *

surface_gallery = parametric_surface()

u_num = 100
v_num = 100
# creating u and v values
u_values = np.linspace(-np.pi, 2*np.pi, u_num)
v_values = np.linspace(-np.pi, 2*np.pi, v_num)

# creating array of vertices
vertices = []
for u in u_values:
    for v in v_values:
        vertex = surface_gallery.trefoil(u, v)
        vertices.append(vertex)

# creating faces
faces = []
counter = 0

for i in range(0, v_num*(u_num - 1)):
    if counter < u_num - 1:
        A = i
        B = i + 1
        C = (i + u_num) + 1
        D = (i + u_num)

        face = (A, B, C, D)
        faces.append(face)
        counter += 1
    else:
        counter = 0

mesh = bpy.data.meshes.new("Trefoil")
object = bpy.data.objects.new("Trefoil", mesh)

object.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(object)

mesh.from_pydata(vertices, [], faces)
mesh.update(calc_edges=True)
