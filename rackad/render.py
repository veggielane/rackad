import trimesh
import pyrender
fuze_trimesh = trimesh.load('outputs/1U19-PANEL-FORMED.stl')
mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
scene = pyrender.Scene()
scene.add(mesh)
pyrender.Viewer(scene, use_raymond_lighting=True)