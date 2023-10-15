"""Textures examples"""

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
from geometry.new_canecageometry import CanecaGeometry
from geometry.new_mesa import MesaGeometry
from geometry.new_cenario import CenarioGeometry

import random 
import pygame
import os



######################################################################################################





    #VEJAM O NEW CANECA GEOMETRY, CENARIO, MESA








#######################################################################################################

BLACK = (0, 0, 0)

class Example(Base):
    """ Render a textured square """

    def initialize(self):
        print("Initializing program...")


        label_geolocation_2 = RectangleGeometry(width=300, height=200, position=[800, 0], alignment=[1,0])
        label_material_2 = TextureMaterial(Texture("images/score.png"))
        label_2 = Mesh(label_geolocation_2, label_material_2)
        self.scene.add(label_2)

        
        self.cup_position = [-1.5, 10, 0]
        # self.table_position = [0.60, 0.60, 0.60]


        # BASIC SETUP
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800 / 600)
        # self.camera.set_position([0.0, 3.5, 20])#posição da camera talvez a melhor


        self.camera.set_position([0.0, 5.5, 2])
        self.rig1 = MovementRig([0.0, 3.5, 20])
        self.rig1.add(self.camera)
        self.rig1.set_position([0.0, 3.5, 20])

        self.rig = self.rig1
        print(self.rig1)




        ambient = AmbientLight(color=[0.5, 0.5, 0.5])
        self.scene.add(ambient)

        directional = DirectionalLight(color=[0.8, 0.8, 0.8], direction=[-1, -1, -2])
        self.scene.add(directional)

        point = PointLight(color=[1.0, 1.0, 1.0], position=[1, 1, 0.8])
        self.scene.add(point)

        self.sky_geometry = RectangleGeometry(width=70, height=30,position=[0, 0])
        self.sky_material = TextureMaterial(texture=Texture(file_name="images/cozinhaf.png"))
        # self.sky = Mesh(self.sky_geometry, self.sky_material)
        self.sky_mesh= CenarioGeometry()# MODO NOVO
        self.sky_mesh.objeto.rotate_y(4.7)
        self.sky_mesh.objeto.scale(4)
        # self.sky.set_position([0.0,10.5, -5.0])
        self.scene.add(self.sky_mesh.objeto)





        
        self.grass_geometry = RectangleGeometry(width=100, height=100)
        self.grass_material = TextureMaterial(
            texture=Texture(file_name="images/floorc.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        self.grass = Mesh(self.grass_geometry,self.grass_material)
        self.grass.rotate_x(-math.pi/2)
        self.scene.add(self.grass)

        #MESA   -----    #################
        texture = Texture(file_name="textures/stone.jpg")
        geometry_mesa = Model('blender/mesa.obj')
        material = TextureMaterial(texture=texture)
        self.mesh_mesa = MesaGeometry()
        self.mesh_mesa.objeto.set_position([0, 0, 0])
        self.mesh_mesa.objeto.scale(4)
        self.mesh_mesa.objeto.rotate_y(11)
        self.scene.add(self.mesh_mesa.objeto)
        # self.rig2 = MovementRig()
        # self.rig2.add(self.mesh_mesa)
        ###################################
        
        #Copo Willian Santos - Autor#################
        texture = Texture(file_name="textures/nescafe_logo.png")
        geometry_copo = Model('blender/nescafemug.obj')
        material = PhongMaterial(property_dict={"baseColor":[0.6, 0.2, 0.2]}, texture=texture)
        self.mesh_copo = CanecaGeometry()
        self.mesh_copo.objeto.set_position([-1.5, 15, 0])
        self.mesh_copo.objeto.scale(0.5)
        # self.mesh_copo.position = self.cup_position
        # self.mesh_copo.scale(0.3)
        # self.mesh_copo.rotate_y(-5)
        self.scene.add(self.mesh_copo.objeto)

        # self.objeto = Object3D()
        # self.objeto.add(self.mesh_copo)

        self.rig3 = MovementRig()
        self.rig3.add(self.mesh_copo.objeto)
        ###################################


        # #Frigideira Andre Singh - Autor#################
        # pizza = PizzaGeometry()
        # material = SurfaceMaterial(property_dict={"useVertexColors": True})
        # #grid_texture = Texture(file_name="images/pizza.png")
        # #material = TextureMaterial(texture=grid_texture,)
        # self.mesh_frigideira =Mesh(geometry=pizza, material=material)
        # self.mesh_frigideira.translate(-1.5, 1.53, 0)
        
        # self.scene.add(self.mesh_frigideira)
        # self.mesh_frigideira.scale(0.50)
        # self.mesh_frigideira.rotate_y(2)
        # self.rig4 = MovementRig()
        # self.rig4.add(self.mesh_frigideira)
        # ###################################
        
        # #Chavena Pedro Ramalho - Autor#################
        # texture = Texture(file_name="textures/wood.jpg")
        # geometry_chavena = Model('blender/chavenav2.obj')
        # material = TextureMaterial(texture=texture)
        # self.mesh_chavena = Mesh(geometry_chavena, material)
        # self.mesh_chavena.set_position([1.5, 1.50, 0])
        # self.mesh_chavena.rotate_y(-11)
        # self.mesh_chavena.scale(0.25)
        # self.scene.add(self.mesh_chavena)
        # self.rig5 = MovementRig()
        # self.rig5.add(self.mesh_chavena)
        # ###################################

        # #Colher João Guerreiro - Autor#################
        # texture = Texture(file_name="textures/inox.png")
        # geometry_colher = Model('blender/spoon.obj')
        # material = TextureMaterial(texture=texture)
        # self.mesh_colher = Mesh(geometry_colher, material)
        # self.mesh_colher.set_position([0.0, 1.53, +0.5])
        # self.mesh_colher.scale(0.05)
        # self.mesh_colher.rotate_z(0.04)
        # self.scene.add(self.mesh_colher)
        # self.rig6 = MovementRig()
        # self.rig6.add(self.mesh_colher)
        # ###################################
        
        # #Garfo- Rafael Escher - Autor#################
        # texture = Texture(file_name="textures/inoxMetalico.jpg")
        # geometry_fork = Model('blender/fork.obj')
        # material = TextureMaterial(texture=texture)
        # self.mesh_fork = Mesh(geometry_fork, material)
        # self.mesh_fork.set_position([1.35, 1.53, 0.5])
        # self.mesh_fork.scale(0.05)
        # self.mesh_fork.rotate_y(3.1)
        # self.mesh_fork.rotate_z(0.05)
        # self.scene.add(self.mesh_fork)
        # self.rig7 = MovementRig()
        # self.rig7.add(self.mesh_fork)
        ###################################
        ### AXIS ###
        # self.axes = AxesHelper()
        # self.scene.add(self.axes)

        ### GRID ###
        grid = GridHelper(
            size=100,
            grid_color=[1, 1, 1],
            center_color=[1, 1, 0]
        )
        grid.rotate_x(-math.pi / 2)
        self.scene.add(grid)
        
    def update(self):
        if self.input.is_key_pressed('tab'):
            self.initialize()


            


        # if self.input.is_key_pressed('1'):
        # self.rig.update(self.input, self.delta_time)
        # if self.input.is_key_pressed('1'):
        #         self.rig = self.rig1   
        # # if self.input.is_key_pressed('2'):
        # #         self.rig = self.rig2   
        # if self.input.is_key_pressed('3'):
        #         self.rig = self.rig3     
        # if self.input.is_key_pressed('4'):
        #         self.rig = self.rig4  
        # if self.input.is_key_pressed('5'):
        #         self.rig = self.rig5  
        # if self.input.is_key_pressed('6'):
        #         self.rig = self.rig6 
        # if self.input.is_key_pressed('7'):
        #         self.rig = self.rig7 
 
        # position = self.rig.get_position()
        # print(position)
        #print(self.table_position[1])
        self.life = 0
        self.score = 0
        self.table_position = self.mesh_mesa.objeto.get_position()
        self.objeto_position = self.mesh_copo.objeto.get_position()



        # if self.input.is_key_pressed('up'):
        #         #    comentar apra mexer a cmaera
        #             if(self.mesh_copo.objeto.global_position[2]< -5.0):
        #                 self.mesh_copo.objeto.translate(0, 0, 0)
        #                 self.camera.translate(0, 0, 0.0)
        #             else:
        #                 # self.mesh_copo.objeto.translate(0, 0, -0.2)#DESCOEMNTAR PARA ANDAR APRA FRENTE COM O COPO
        #                 self.camera.translate(0, 0, -0.1)
                    
        # if self.input.is_key_pressed('down'):
        #             self.mesh_copo.objeto.translate(0, 0, 0.2)
        #             self.camera.translate(0, 0, 0.1)





        
###########################################################################################

# nao sei pq quando enconta no limite da um bug qualquer 
# acho que tem de esta no intervalo  a >x<b  não sei ainda
#ajudaaa

###########################################################################################

                    
        # if self.input.is_key_pressed('left'):
        #         # self.camera.translate(-0.1,0, 0)#teste apenas
        #         if( self.mesh_copo.objeto.global_position[0]<-38):
        #                 self.mesh_copo.objeto.translate(0, 0, 0)
        #                 self.camera.translate(0, 0, 0.0)

        #         else:
        #             # self.mesh_copo.objeto.translate(-0.2,0, 0)
        #             self.mesh_copo.objeto.translate(-0.2,0, 0)#teste apenas

        #             # self.camera.translate(-0.1,0, 0)
        #             self.camera.translate(-0.2,0, 0)#teste apenas

        # if self.input.is_key_pressed('right'):
                    
        #             if(self.mesh_copo.objeto.global_position[0]>39):
        #                 self.mesh_copo.objeto.translate(0, 0, 0)
        #                 self.camera.translate(0, 0, 0.0)
        #             else:
        #                 self.mesh_copo.objeto.translate(0.2, 0, 0)
        #                 self.camera.translate(0.1, 0, 0)    
        if self.input.is_key_pressed('a'):
                if( self.mesh_copo.objeto.global_position[0]<-38):
                        self.mesh_copo.objeto.translate(0, 0, 0)

                else:
                    self.mesh_copo.objeto.translate(-0.2,0, 0)

        if self.input.is_key_pressed('d'):
                    
                    if(self.mesh_copo.objeto.global_position[0]>39):
                        self.mesh_copo.objeto.translate(0, 0, 0)
                    else:
                        self.mesh_copo.objeto.translate(0.2, 0, 0)  

        if self.input.is_key_pressed('s'):
                    
                    if(self.mesh_copo.objeto.global_position[0]>39):
                        self.mesh_copo.objeto.translate(0, 0, 0)
                    else:
                        self.mesh_copo.objeto.translate(0.0, 0, 0.2)  

        if self.input.is_key_pressed('w'):
                    
                    if(self.mesh_copo.objeto.global_position[0]>39):
                        self.mesh_copo.objeto.translate(0, 0, 0)
                    else:
                        self.mesh_copo.objeto.translate(0.0, 0, -0.2)  

        
        if self.input.is_key_pressed('up'):
                #    comentar apra mexer a cmaera
                    if(self.mesh_copo.objeto.global_position[2]< -5.0):
                    
                        self.camera.translate(0, 0, 0.0)
                    else:
                        # self.mesh_copo.objeto.translate(0, 0, -0.2)#DESCOEMNTAR PARA ANDAR APRA FRENTE COM O COPO
                        self.camera.translate(0, 0, -0.1)
                    
        if self.input.is_key_pressed('down'):
                    self.camera.translate(0, 0, 0.1)

        if self.input.is_key_pressed('left'):
                # self.camera.translate(-0.1,0, 0)#teste apenas
                self.hah = self.camera.global_position[0]
                print(self.hah)
                if( self.hah < -33.2000000000002):
                        self.camera.translate(0, 0, 0.0)
                else:
                    self.camera.translate(-0.2,0, 0)#teste apenas   

        if self.input.is_key_pressed('right'):
                    
                    if(self.mesh_copo.objeto.global_position[0]>39):
                        self.camera.translate(0, 0, 0.0)
                    else:
                        self.camera.translate(0.1, 0, 0)

        if self.input.is_key_pressed('1'):
                 
                    self.mesh_copo.objeto.translate(0, 0.1, 0)#MERAMENTE APRA TESTE E ENCONTRAR ALTURA DA MESA
        if self.input.is_key_pressed('2'):
                 
                    self.mesh_copo.objeto.translate(0, -0.1, 0)#MERAMENTE APRA TESTE E ENCONTRAR ALTURA DA MESA

                  

###########################################################################################

                    ####        descomentar a baixo para o objeto cair              ######
        # self.mesh_copo.objeto.translate(0,-0.1,0) # decrease y-coordinate by 0.01 on each frame

###########################################################################################

        # agora isto e para ver se esta na mesa começo


        # self.x_mesa=  self.mesh_mesa.objeto.global_position[0]#busca o x da mesa no momento
        # self.z_mesa=  self.mesh_mesa.objeto.global_position[1]#busca o z da mesa no momento
        # self.y_mesa=6.049999999999908 #altura atual da mesa# y da mesa

        # if 


###########################################################################################



        #SE TOCAR NO CHAO
        if self.mesh_copo.objeto.global_position[1] < 0:
        #olha ta aqui
                pygame.time.delay(200)# DA DELAY APOS TOCAR NO CHAO
                # self.mesh_copo.objeto.set_position([-1.5, 20, 0]) 
                self.xrandom = random.uniform(-20 , 20)
                self.zrandom =random.uniform(0, 10)
                
                self.mesh_copo.objeto.set_position([self.xrandom,15,self.zrandom ] ) #teleport caneca
                self.camera.set_position([self.xrandom, 3.5,self.zrandom])
                
                # self.mesh_mesa.objeto.set_position([ random.uniform(-20 , 20),0,  random.uniform(0, 10) ])# teleport mesa




             
        # self.font = pygame.font.Font(None, 36  )      
        # self.text = self.font.render("Score: " + str(self.score), True, BLACK)





                       
               
        # if self.rig == self.rig3:
        
        # if self.cup_position[1] <= 1.5 and -0.5 <= position[0] <= 3.5: #and -0.5 <= position[3] <= 3.5 :

        #         self.cup_position = [-1.5, 10, 0]
        # elif self.cup_position[1] < 0: # if cup hits the ground
        #         self.cup_position = [-1.5, 10, 0]
        # self.mesh_copo.set_position(self.cup_position)

        
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
# Example(screen_size=[900, 800]).run()
Example(screen_size=[800, 600]).run()
