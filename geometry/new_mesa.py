
import numpy as np
import math
import pathlib
import sys

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from extras.axes import AxesHelper
from core_ext.object3d import Object3D

from material.surface import SurfaceMaterial
from material.texture import TextureMaterial
from material.basic import BasicMaterial
from extras.grid import GridHelper
from extras.movement_rig import MovementRig

from geometry.model import Model
from geometry.pizza import PizzaGeometry
from geometry.rectangle import RectangleGeometry
from geometry.sphere import SphereGeometry
from geometry.cylinder import CylinderGeometry
from geometry.rectangle import RectangleGeometry

from light.ambient import AmbientLight
from light.directional import DirectionalLight
from light.point import PointLight


from material.surface import SurfaceMaterial
from material.flat import FlatMaterial
from material.lambert import LambertMaterial
from material.phong import PhongMaterial

import pygame
import sys
from geometry.geometry import Geometry
from geometry.cylinder import CylinderGeometry
from core_ext.mesh import Mesh
from core_ext.object3d import Object3D




class MesaGeometry(Geometry):
    def __init__(self):
        # self.texture = Texture(file_name="textures/nescafe_logo.png")
        # self.geometry_copo = Model('blender/nescafemug.obj')
        # self.material = PhongMaterial(property_dict={"baseColor":[0.6, 0.2, 0.2]}, texture=self.texture)
       
        # self.mesh_copo = Mesh(self.geometry_copo, self.material)

        self.texture = Texture(file_name="textures/stone.jpg")
        self.geometry_mesa = Model('blender/mesa.obj')
        # self.material = TextureMaterial(texture=self.texture)
        self.material = PhongMaterial(texture=self.texture)
        self.mesh_mesa = Mesh(self.geometry_mesa, self.material)

        self.objeto = Object3D()
        self.objeto.add(self.mesh_mesa)
