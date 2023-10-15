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
from geometry.new_frigideira import FrigideiraGeometry

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
from material.texture import TextureMaterial
from core_ext.texture import Texture
import random 
import pygame

from extras.text_texture import TextTexture
from core.base import Base
from core.matrix import Matrix
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from geometry.rectangle import RectangleGeometry
from geometry.box import BoxGeometry
from material.texture import TextureMaterial
from extras.movement_rig import MovementRig
from extras.grid import GridHelper
from geometry.new_chavena import ChavenaGeometry


######################################################################################################





    #VEJAM O NEW CANECA GEOMETRY, CENARIO, MESA








#######################################################################################################

pygame.font.init()

class Example(Base):
    """ Render a textured square """

    def initialize(self):
        print("Initializing program...")


        
        self.cup_position = [-1.5, 10, 0]
        # self.table_position = [0.60, 0.60, 0.60]


        # BASIC SETUP
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800 / 600)
        # self.camera.set_position([0.0, 3.5, 20])#posição da camera talvez a melhor

        self.hud_scene = Scene()
        self.hud_camera = Camera()
        self.hud_camera.set_orthographic(0, 800, 0, 600, 1, -1)



        self.camera.set_position([0.0, 5.5, 2])
        self.rig1 = MovementRig([0.0, 3.5, 20])
        self.rig1.add(self.camera)
        self.rig1.set_position([0.0, 3.5, 20])
        # self.rig1.rotate_x(-0.3)

        # self.rig = self.rig1
        # print(self.rig1)




        ambient = AmbientLight(color=[0.5, 0.5, 0.5])
        self.scene.add(ambient)

        directional = DirectionalLight(color=[0.8, 0.8, 0.8], direction=[-1, -1, -2])
        self.scene.add(directional)

        point = PointLight(color=[1.0, 1.0, 1.0], position=[1, 1, 0.8])
        self.scene.add(point)

        # self.sky_geometry = RectangleGeometry(width=70, height=30,position=[0, 0])
        # self.sky_material = TextureMaterial(texture=Texture(file_name="images/cozinhaf.png"))
        # # self.sky = Mesh(self.sky_geometry, self.sky_material)
        # self.sky_mesh= CenarioGeometry()# MODO NOVO
        # self.sky_mesh.objeto.rotate_y(4.7)
        # self.sky_mesh.objeto.scale(4)
        # # self.sky.set_position([0.0,10.5, -5.0])
        # self.scene.add(self.sky_mesh.objeto)


        
        # self.texture_inicio = Texture (file_name="images/inicio.png")
        # self.inicio_geometry = Model('blender/menu.obj')
        # self.material_inicio = TextureMaterial( texture=self.texture_inicio)
        # self.mesh_menu = Mesh( self.inicio_geometry, self.material_inicio)
        # # self.mesh_menu.set_position([-70.20000000000046, 0,0])
        # self.mesh_menu.rotate_y(-1.58)
        # self.mesh_menu.set_position([0,2,0])
        # self.mesh_menu.scale(7)
        # self.scene.add(self.mesh_menu)

        self.menu_geolocation = RectangleGeometry(width=800, height=600, position=[0, 600], alignment=[0,1])
        self.menu_material = TextureMaterial(Texture("images/inicio.png"))
        self.menu_label = Mesh(self.menu_geolocation, self.menu_material)
        self.hud_scene.add(self.menu_label)




        
        # self.grass_geometry = RectangleGeometry(width=100, height=100)
        # self.grass_material = TextureMaterial(
        #     texture=Texture(file_name="images/floorc.jpg"),
        #     property_dict={"repeatUV": [50, 50]}
        # )
        # self.grass = Mesh(self.grass_geometry,self.grass_material)
        # self.grass.rotate_x(-math.pi/2)
        # self.scene.add(self.grass)

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

        self.score = 11



        label_texture = TextTexture(text=" This is a Crate. ",
                                system_font_name="Arial Bold",
                                    font_size=40, font_color=[0, 0, 200],
                                    image_width=256, image_height=128,
                                    align_horizontal=0.5, align_vertical=0.5,
                                    image_border_width=4,
                                    image_border_color=[255, 0, 0])

        # label_material = TextureMaterial(label_texture)
        # label_geometry = RectangleGeometry(width=1, height=0.5)
        # label_geometry.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        # self.label = Mesh(label_geometry, label_material)
        # self.scene.add(self.label)
       
         
        self.label_geolocation_1 = RectangleGeometry(width=400, height=80, position=[0, 600], alignment=[0,1])
        self.label_material_1 = TextureMaterial(TextTexture(text="Score "+ str(self.score),
                                    system_font_name="Press Start 2P",
                                    font_size=80, font_color=[0, 0, 0],transparent=True,
                                    image_width=600, image_height=128,
                                    align_horizontal=0.5, align_vertical=0.5,
                                    image_border_width=0))
        self.label_1 = Mesh(self.label_geolocation_1, self.label_material_1)
        self.hud_scene.add(self.label_1)


        # #Chavena Pedro Ramalho - Autor#################
        texture = Texture(file_name="textures/wood.jpg")
        geometry_chavena = Model('blender/chavenav2.obj')
        material = TextureMaterial(texture=texture)
        self.mesh_chavena = ChavenaGeometry()
        self.mesh_chavena.objeto.set_position([1.5, 25, 0])
        self.mesh_chavena.objeto.scale(1.0)
        self.scene.add(self.mesh_chavena.objeto)

        self.rig5 = MovementRig()
        self.rig5.add(self.mesh_chavena.objeto)
        # ###################################

         #Frigideira Andre Singh - Autor#################
        texture = Texture(file_name="textures/dark-metal.jpg")
        geometry_frigideira = Model('blender/frigideira.obj')
        material = PhongMaterial(property_dict={"baseColor":[0.6, 0.2, 0.2]}, texture=texture)
        self.mesh_frigideira = FrigideiraGeometry()
        self.mesh_frigideira.objeto.set_position([-1.5, 25, 0])
        self.mesh_frigideira.objeto.scale(1.5)
        # self.mesh_copo.position = self.cup_position
        # self.mesh_copo.scale(0.3)
        # self.mesh_copo.rotate_y(-5)
        self.scene.add(self.mesh_frigideira.objeto)





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
      
       
        self.c =0

     
        # self.scene.add(self.score_text)
    
        self.table_position = self.mesh_mesa.objeto.get_position()
        self.objeto_position = self.mesh_copo.objeto.get_position()
        print( self.objeto_position)
        # self.objeto_position = self.mesh_chavena.objeto.get_position()
        # self.objeto_position = self.mesh_frigideira.objeto.get_position()
        

        if self.input.is_key_pressed('up'):    

                #    comentar apra mexer a cmaera
                    if(self.mesh_copo.objeto.global_position[2]< -5.0):
                        self.mesh_copo.objeto.translate(0, 0, 0)
                        self.camera.translate(0, 0, 0.0)
                    else:
                        # self.mesh_copo.objeto.translate(0, 0, -0.2)#DESCOEMNTAR PARA ANDAR APRA FRENTE COM O COPO
                        self.camera.translate(0, 0, -0.1)
                    
        if self.input.is_key_pressed('down'):
                    self.mesh_copo.objeto.translate(0, 0, 0.2)
                    self.camera.translate(0, 0, 0.1)                    
        if self.input.is_key_pressed('a'):
                if( self.mesh_copo.objeto.global_position[0]<-38):
                        self.mesh_copo.objeto.translate(0, 0, 0)

                else:
                    self.mesh_copo.objeto.translate(-0.5,0, 0)

        if self.input.is_key_pressed('d'):
                    
                    if(self.mesh_copo.objeto.global_position[0]>39):
                        self.mesh_copo.objeto.translate(0, 0, 0)
                    else:
                        self.mesh_copo.objeto.translate(0.5, 0, 0)  

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
        
        if self.input.is_key_pressed('q'):
                    
        
                self.mesh_copo.objeto.translate(0, 0.1, 0)
    
        
        if self.input.is_key_pressed('e'):
                    

                self.mesh_copo.objeto.translate(0, -0.1, 0)
                                                        

        if self.input.is_key_pressed('left'):
                # self.camera.translate(-0.1,0, 0)#teste apenas
                if( self.mesh_copo.objeto.global_position[0]<-38):
                        self.camera.translate(0, 0, 0.0)
                else:
                    self.camera.translate(-0.2,0, 0)#teste apenas   

        if self.input.is_key_pressed('right'):
                    
                    if(self.mesh_copo.objeto.global_position[0]>39):
                        self.camera.translate(0, 0, 0.0)
                    else:
                        self.camera.translate(0.1, 0, 0) 











            


        # if self.input.is_key_pressed('1'):
                 
        #             self.mesh_copo.objeto.translate(0, 0.1, 0)#MERAMENTE APRA TESTE E ENCONTRAR ALTURA DA MESA
        # if self.input.is_key_pressed('2'):
                 
        #             self.mesh_copo.objeto.translate(0, -0.1, 0)#MERAMENTE APRA TESTE E ENCONTRAR ALTURA DA MESA

                  

###########################################################################################

                    ####        descomentar a baixo para o objeto cair              ######
        # self.mesh_copo.objeto.translate(0,-0.1,0) # decrease y-coordinate by 0.01 on each frame

###########################################################################################

        # agora isto e para ver se esta na mesa começo


        self.x_mesa=  self.mesh_mesa.objeto.global_position[0]#busca o x da mesa no momento
        self.z_mesa=  self.mesh_mesa.objeto.global_position[2]#busca o z da mesa no momento
        self.y_mesa=6.049999999999908 #altura atual da mesa# y da mesa




###########################################################################################

        self.y_copo = self.mesh_copo.objeto.global_position[1]
        self.x_copo = self.mesh_copo.objeto.global_position[0]
        self.z_copo = self.mesh_copo.objeto.global_position[2]
        i = 0



        #SE TOCAR NO CHAO
        if self.mesh_copo.objeto.global_position[1] < 0:#decres
        #olha ta aqui
                pygame.time.delay(200)# DA DELAY APOS TOCAR NO CHAO
                
                self.mesh_copo.objeto.set_position([random.uniform(-20 , 20),15,random.uniform(0, 10) ] ) #teleport caneca
                self.camera.set_position([0.0, 3.5, 20])
                self.mesh_mesa.objeto.set_position([ random.uniform(-20 , 20),0,  random.uniform(0, 10) ])# teleport mesa

        # if self.y_copo == self.y_mesa and self.x_mesa - 7 < self.x_copo < self.x_mesa + 7 and self.z_mesa - 3 < self.z_copo < self.z_mesa + 3:
        #         #olha ta aqui
        #         pygame.time.delay(200)# DA DELAY APOS TOCAR NO CHAO
        #         self.xrandom = random.uniform(-20 , 20)
        #         self.zrandom =random.uniform(0, 10) 
        #         self.mesh_copo.objeto.set_position([ self.xrandom,15,self.zrandom ] ) #teleport caneca
        #         self.camera.set_position([self.xrandom, 3.5,self.zrandom])
                
        #         self.mesh_mesa.objeto.set_position([ random.uniform(-20 , 20),0,  random.uniform(0, 10) ])# teleport mesa

            
        #         self.score +=1
        #         self.hud_scene.remove(self.label_1)         
        #         self.label_geolocation_1 = RectangleGeometry(width=400, height=80, position=[0, 600], alignment=[0,1])
        #         self.label_material_1 = TextureMaterial(TextTexture(text="Score "+ str(self.score),
        #                                         system_font_name="Press Start 2P",
        #                                         font_size=80, font_color=[0, 0, 0],transparent=True,
        #                                         image_width=600, image_height=128,
        #                                         align_horizontal=0.5, align_vertical=0.5,
        #                                         image_border_width=0))
        #         self.label_1 = Mesh(self.label_geolocation_1, self.label_material_1)
        #         self.hud_scene.add(self.label_1)


                # label_geolocation_1 = RectangleGeometry(width=600, height=80, position=[0, 600], alignment=[0, 1])
                # label_material_1 = TextureMaterial(TextTexture(text=str(self.score), transparent=True, image_width=600, font_size=8))
                # self.label_1 = Mesh(label_geolocation_1, label_material_1)
                # self.hud_scene.add(self.label_1)



       


        
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(self.hud_scene, self.hud_camera, clear_color=False)


# Instantiate this class and run the program
Example(screen_size=[900, 800]).run()
# Example(screen_size=[800, 600]).run()