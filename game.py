
"""Textures examples"""

import numpy as np
import math
import pathlib
import sys
from ast import Delete

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from extras.axes import AxesHelper
from core_ext.object3d import Object3D

import time
import random

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
from geometry.new_canecageometry import CanecaGeometry

from light.ambient import AmbientLight
from light.directional import DirectionalLight
from light.point import PointLight


from material.surface import SurfaceMaterial
from material.flat import FlatMaterial
from material.lambert import LambertMaterial
from material.phong import PhongMaterial


# from random import *
import pygame
import sys

class Example(Base):
    """ Render a textured square """

    def initialize(self):
        print("Initializing program...")
        self.lastSecond = time.time()

        # BASIC SETUP
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800 / 600)
        self.cameraRig = MovementRig(degrees_per_second=20)

        #RIG PARA A CAMERA DEPOIS TIRAR ISTO
        self.cameraRig.add(self.camera)
        self.camera.translate(0, 10, 30)

        #Tens de ver isto melhor##########################################################################################################
        ambient = AmbientLight(color=[0.5, 0.5, 0.5])
        self.scene.add(ambient)
        directional = DirectionalLight(color=[0.8, 0.8, 0.8], direction=[-1, -1, -2])
        self.scene.add(directional)
        point = PointLight(color=[1.0, 1.0, 1.0], position=[1, 1, 0.8])
        self.scene.add(point)
##########################################################################################################################################



        self.itens = [] # Certifique-se de que este atributo é definido corretamente
        self.ItensInfo = []
#########################################################################################################
        self.sky_geometry = RectangleGeometry(width=70, height=30,position=[0, 0])                      #
        self.sky_material = TextureMaterial(texture=Texture(file_name="images/cozinhaf.png"))           #
        self.sky = Mesh(self.sky_geometry, self.sky_material)                                           #
        self.sky.set_position([0.0,10.5, -5.0])                                                         #
        self.scene.add(self.sky)                                                                        #
        self.grass_geometry = RectangleGeometry(width=100, height=100)                                  #
        self.grass_material = TextureMaterial(                                                          #    SKY BOX
            texture=Texture(file_name="images/floorc.jpg"),                                             #
            property_dict={"repeatUV": [50, 50]}                                                        #
        )                                                                                               #
        self.grass = Mesh(self.grass_geometry,self.grass_material)                                      #
        self.grass.rotate_x(-math.pi/2)                                                                 #
        self.scene.add(self.grass)                                                                      #
#########################################################################################################
        #MESA############################################
        self.scene.add(self.criarMesa())                #
        #################################################
        self.scene.add(self.criarCopo())

        #  POSIÇÃO INICAL DOS OBJETOS
        self.countFrames = int(0)
        self.lastSecondFrames = int(0)
        self.ObjetosCair = []
        self.toClean = []
        
    def criarCopo(self):
        texture = Texture(file_name="textures/nescafe_logo.png")
        geometry_copo = Model('blender/nescafemug.obj')
        material = TextureMaterial(texture=texture)
        mesh_copo = Mesh(geometry_copo, material)
        mesh_copo.set_position([0, -4, 0])
        mesh_copo.scale(0.3)
        mesh_copo.rotate_y(-5)
        return mesh_copo


    def update(self):
        self.cairObjetos()
        self.countFrames += 1
        self.lastSecondFrames += 1
        if( (time.time() - self.lastSecond) > 1):
            print("\nFrames got last second is")
            print(self.lastSecondFrames)
            self.lastSecondFrames = int(0)
            self.lastSecond = time.time()
            self.cleanObjects()

        self.cameraRig.update(input_object=self.input,delta_time=0.1)
        self.renderer.render(self.scene, self.camera)
        if self.input.is_key_pressed('tab'):
            # self.initialize()
             pygame.quit()
             sys.exit()
        # if self.input.is_key_pressed('p'):

        if self.countFrames % 60 == 0 :
            # tempVar = self.criarCopo()
            self.templist= self.getListaDeItens()
            self.tempVar = self.templist[0]
            self.tempVar.set_position([ random.uniform(-20 , 20), random.uniform(0, 20) , 0])
            self.ObjetosCair.append(self.tempVar)
            self.scene.add(self.tempVar)

    def cairObjetos(self):
        for objeto in self.ObjetosCair:
            objeto.translate(0,-0.2,0)
            if( 0 > objeto.global_position[1] ):
                self.ObjetosCair.remove(objeto)
                self.toClean.append(objeto)

    def cleanObjects(self):
        for objeto in self.toClean:
            self.toClean.remove(objeto)
            self.scene.remove(objeto)
            Delete(objeto)

    def criarMesa(self):
        texture = Texture(file_name="textures/stone.jpg")           #
        geometry_mesa = Model('blender/mesa.obj')                   #
        material = TextureMaterial(texture=texture)                 #
        mesh_mesa = Mesh(geometry_mesa, material)              #
        mesh_mesa.set_position([0, 0, 0])                      #
        mesh_mesa.scale(1)                                     #
        mesh_mesa.rotate_y(11)                                 #
        return mesh_mesa



    def lista_de_itens(self, lista_inicial = 10):
        self.itens=[]
        self.ItensInfo= []
        self.randomItens()
    #apenas gera canecas teste apenas
    def randomItens(self, lista_inicial= 10):
        for i in range( 0, lista_inicial):
            tipo = random.randint(0,2)
            self.ItensInfo.append(tipo+1 if tipo != 2 else 2)            
            if tipo == 0:
                self.itens.append(self.criarCopo())
            elif tipo == 1:
                self.itens.append(self.criarCopo())
            elif tipo == 2:
                self.itens.append(self.criarCopo())
    # se não
    #  tiver itens ggera dois novos random e adiciona            
    def getListaDeItens(self):
        if not self.itens:
            self.randomItens(lista_inicial= 10)
        return [self.itens.pop(0)]
    def addItens(self, item, ItensInfo):
        item.set_Position([0,0,0])
        rand = random.randint(0, len(self.itens))
        self.itens.insert(rand, item)
        self.ComidaInfo.insert(rand, ItensInfo)









# Instantiate this class and run the program
Example(screen_size=[1200, 800]).run()