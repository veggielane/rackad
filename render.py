import trimesh
import pyrender
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
os.environ['PYOPENGL_PLATFORM'] = 'osmesa'
fuze_trimesh = trimesh.load('outputs/1U10-PANEL-FORMED.stl')
mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
scene = pyrender.Scene()
scene.add(mesh)

camera = pyrender.OrthographicCamera(xmag=200.0, ymag=200.0, zfar=1000.0,znear=0.1)
camera_pose = np.array([
   [1.0, 0.0, 0.0, 0],
   [0.0, 1.0, 0.0, 0],
   [0.0, 0.0, 1.0, 800.0],
   [0.0, 0.0, 0.0, 1.0],
])
scene.add(camera, pose=camera_pose)
#pyrender.Viewer(scene, use_raymond_lighting=True)


r = pyrender.OffscreenRenderer(400, 400)
color, depth = r.render(scene)
img = Image.fromarray(color)
img.save(f"outputs/1U10-PANEL-FORMED.png")