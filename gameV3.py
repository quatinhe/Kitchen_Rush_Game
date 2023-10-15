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
        self.rig1.set_position([0.0, 13, 20])
        self.rig1.rotate_x(-0.5)

        # self.rig = self.rig1
        # print(self.rig1)




        ambient = AmbientLight(color=[0.8, 0.8, 0.8])
        self.scene.add(ambient)

        directional = DirectionalLight(color=[0.9, 0.9, 1], direction=[0, 0, -10])
        self.scene.add(directional)

        point = PointLight(color=[1.0, 1.0, 1.0], position=[0, 20, 0])
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

        self.score = 0
        self.vidas = 3
     



      
         
        self.label_geolocation_1 = RectangleGeometry(width=400, height=80, position=[0, 550], alignment=[0,1])
        self.label_material_1 = TextureMaterial(TextTexture(text="Score "+ str(self.score),
                                    system_font_name="Press Start 2P",
                                    font_size=80, font_color=[0, 0, 0],transparent=True,
                                    image_width=600, image_height=128,
                                    align_horizontal=0.5, align_vertical=0.5,
                                    image_border_width=0))
        self.label_1 = Mesh(self.label_geolocation_1, self.label_material_1)
        # self.hud_scene.add(self.label_1)


        self.label_geolocation_2 = RectangleGeometry(width=60, height=40, position=[600, 550], alignment=[0,1])
        self.label_material_2 = TextureMaterial(Texture("images/coracao.png"))
        self.label_2 = Mesh(self.label_geolocation_2, self.label_material_2)
        # self.hud_scene.add(self.label_2)

        self.label_geolocation_3= RectangleGeometry(width=60, height=40, position=[650, 550], alignment=[0,1])
        self.label_material_3 = TextureMaterial(Texture("images/coracao.png"))
        self.label_3 = Mesh(self.label_geolocation_3, self.label_material_3)
        # self.hud_scene.add(self.label_3)


        self.label_geolocation_4 = RectangleGeometry(width=60, height=40, position=[700, 550], alignment=[0,1])
        self.label_material_4 = TextureMaterial(Texture("images/coracao.png"))
        self.label_4 = Mesh(self.label_geolocation_4, self.label_material_4)
        # self.hud_scene.add(self.label_4)

        self.allH = [self.label_2, self.label_3, self.label_4, self.label_1 ]
        # self.allH.append(self.label_2)
        # self.all[0]= self.label_2
        # self.all[1]= self.label_2
        # self.all[3]= self.label_2
        self.count = 0 

        
        self.menu_geolocation = RectangleGeometry(width=800, height=600, position=[0, 600], alignment=[0,1])
        self.menu_material = TextureMaterial(Texture("images/inicio.png"))
        self.menu_label = Mesh(self.menu_geolocation, self.menu_material)
        self.hud_scene.add(self.menu_label)







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
        #grid.rotate_x(-math.pi / 2)
        #self.scene.add(grid)
        self.activate = True
        self.music = pygame.mixer.Sound("music/start.mp3")
        self.anchivement = pygame.mixer.Sound("music/achievement.wav")
        self.gameover = pygame.mixer.Sound("music/arcade.wav")
        pygame.mixer.Sound.play(self.music,loops=-1)

    def update(self):
        if self.input.is_key_pressed('tab'):
            self.initialize()
            #pygame.mixer.Sound.stop(self.music)

        self.life = 1
        self.c =0
        # self.scene.add(self.score_text)
        self.table_position = self.mesh_mesa.objeto.get_position()
        self.objeto_position = self.mesh_copo.objeto.get_position()
        self.objeto_position = self.mesh_chavena.objeto.get_position()
        self.objeto_position = self.mesh_frigideira.objeto.get_position()
        if self.input.is_key_pressed('r'):
           

            self.activate = False
            
            self.hud_scene.remove(self.menu_label)
                    
            # self.label_geolocation_5 = RectangleGeometry(width=400, height=80, position=[200, 400], alignment=[0,1])
            # self.label_material_5 = TextureMaterial(TextTexture(text=" GO !!!",
            #                             system_font_name="Press Start 2P",
            #                             font_size=80, font_color=[0, 0, 0],transparent=True,
            #                             image_width=600, image_height=128,
            #                             align_horizontal=0.5, align_vertical=0.5,
            #                             image_border_width=0))
            # self.label_5 = Mesh(self.label_geolocation_5, self.label_material_5)
            # self.hud_scene.add(self.label_5)

            self.hud_scene.add( self.allH[0])
            self.hud_scene.add( self.allH[1])
            self.hud_scene.add( self.allH[2])
            self.hud_scene.add( self.allH[3])
            # pygame.time.delay(2000)
          
            pygame.time.wait(2000)
        if self.activate == False: 
            # self.hud_scene.remove(self.label_5)  
          
            if self.vidas > 0:
                if ( self.score <= 5):
                    if self.input.is_key_pressed('up'):    
                            #    comentar apra mexer a cmaera
                                if(self.camera.global_position[2]< -5.0):
                                    # self.mesh_copo.objeto.translate(0, 0, 0)
                                    self.camera.translate(0, 0, 0.0)
                                else:
                                    # self.mesh_copo.objeto.translate(0, 0, -0.2)#DESCOEMNTAR PARA ANDAR APRA FRENTE COM O COPO
                                    self.camera.translate(0, 0.05, -0.1)
                                
                    if self.input.is_key_pressed('down'):
                                self.camera.translate(0, -0.05, 0.1)                    
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
                    if self.input.is_key_pressed('left'):
                            # self.camera.translate(-0.1,0, 0)#teste apenas
                            if( self.camera.global_position[0]<-38):
                                    self.camera.translate(0, 0, 0.0)
                            else:
                                self.camera.translate(-0.2,0, 0)#teste apenas   
                    if self.input.is_key_pressed('right'):
                                
                                if(self.hud_camera.global_position[0]>39):
                                    self.camera.translate(0, 0, 0.0)
                                else:
                                    self.camera.translate(0.2, 0, 0) 
                elif ( 5 < self.score <= 10 ):
                    self.mesh_copo.objeto.set_position([-1.5, 30, 0])
                    if self.input.is_key_pressed('up'):    
                            #    comentar apra mexer a cmaera
                                if(self.camera.global_position[2]< -5.0):
                                    # self.mesh_chavena.objeto.translate(0, 0, 0)
                                    self.camera.translate(0, 0, 0.0)
                                else:
                                    # self.mesh_copo.objeto.translate(0, 0, -0.2)#DESCOEMNTAR PARA ANDAR APRA FRENTE COM O COPO
                                    self.camera.translate(0, 0.05, -0.1)
                                
                    if self.input.is_key_pressed('down'):
                                # self.mesh_chavena.objeto.translate(0, 0, 0.2)
                                self.camera.translate(0, -0.05, 0.1)   
                    if self.input.is_key_pressed('d'):
                            if( self.mesh_chavena.objeto.global_position[0]<-38):
                                    self.mesh_chavena.objeto.translate(0, 0, 0)
                            else:
                                self.mesh_chavena.objeto.translate(-0.5,0, 0)
                    if self.input.is_key_pressed('a'):
                                
                                if(self.mesh_chavena.objeto.global_position[0]>39):
                                    self.mesh_chavena.objeto.translate(0, 0, 0)
                                else:
                                    self.mesh_chavena.objeto.translate(0.5, 0, 0)  
                    if self.input.is_key_pressed('s'):
                                
                                if(self.mesh_chavena.objeto.global_position[0]>39):
                                    self.mesh_chavena.objeto.translate(0, 0, 0)
                                else:
                                    self.mesh_chavena.objeto.translate(0.0, 0, 0.2)  
                    if self.input.is_key_pressed('w'):
                                
                                if(self.mesh_chavena.objeto.global_position[0]>39):
                                    self.mesh_chavena.objeto.translate(0, 0, 0)
                                else:
                                    self.mesh_chavena.objeto.translate(0.0, 0, -0.2)  
                    if self.input.is_key_pressed('left'):
                            # self.camera.translate(-0.1,0, 0)#teste apenas
                            if( self.camera.global_position[0]<-38):
                                    self.camera.translate(0, 0, 0.0)
                            else:
                                self.camera.translate(-0.2,0, 0)#teste apenas   
                    if self.input.is_key_pressed('right'):
                                
                                if(self.camera.global_position[0]>39):
                                    self.camera.translate(0, 0, 0.0)
                                else:
                                    self.camera.translate(0.2, 0, 0) 
                elif self.score > 10:
                    self.mesh_chavena.objeto.set_position([-1.5, 30, 0])
                    self.mesh_copo.objeto.set_position([-1.5, 30, 0])
                    if self.input.is_key_pressed('up'):    
                            #    comentar apra mexer a cmaera
                                if(self.camera.global_position[2]< -5.0):
                                    # self.mesh_frigideira.objeto.translate(0, 0, 0)
                                    self.camera.translate(0, 0, 0.0)
                                else:
                                    # self.mesh_copo.objeto.translate(0, 0, -0.2)#DESCOEMNTAR PARA ANDAR APRA FRENTE COM O COPO
                                    self.camera.translate(0, 0.05, -0.1)
                    if self.input.is_key_pressed('down'):
                                # self.mesh_frigideira.objeto.translate(0, 0, 0.2)
                                self.camera.translate(0, -0.05, 0.1)   
                    if self.input.is_key_pressed('a'):
                            if( self.mesh_frigideira.objeto.global_position[0]<-38):
                                    self.mesh_frigideira.objeto.translate(0, 0, 0)
                            else:
                                self.mesh_frigideira.objeto.translate(-0.5,0, 0)
                    if self.input.is_key_pressed('d'):
                                
                                if(self.mesh_frigideira.objeto.global_position[0]>39):
                                    self.mesh_frigideira.objeto.translate(0, 0, 0)
                                else:
                                    self.mesh_frigideira.objeto.translate(0.5, 0, 0)  
                    if self.input.is_key_pressed('w'):
                                
                                if(self.mesh_frigideira.objeto.global_position[0]>39):
                                    self.mesh_frigideira.objeto.translate(0, 0, 0)
                                else:
                                    self.mesh_frigideira.objeto.translate(0.0, 0, -0.2)  
                    if self.input.is_key_pressed('s'):
                                
                                if(self.mesh_frigideira.objeto.global_position[0]>39):
                                    self.mesh_frigideira.objeto.translate(0, 0, 0)
                                else:
                                    self.mesh_frigideira.objeto.translate(0.0, 0, 0.2)  
                    if self.input.is_key_pressed('left'):
                            # self.camera.translate(-0.1,0, 0)#teste apenas
                            if( self.camera.global_position[0]<-38):
                                    self.camera.translate(0, 0, 0.0)
                            else:
                                self.camera.translate(-0.2,0, 0)#teste apenas   
                    if self.input.is_key_pressed('right'):
                                
                                if(self.camera.global_position[0]>39):
                                    self.camera.translate(0, 0, 0.0)
                                else:
                                    self.camera.translate(0.2, 0, 0) 
                # if self.input.is_key_pressed('1'):
                        
                #             self.mesh_copo.objeto.translate(0, 0.1, 0)#MERAMENTE APRA TESTE E ENCONTRAR ALTURA DA MESA
                # if self.input.is_key_pressed('2'):
                        
                #             self.mesh_copo.objeto.translate(0, -0.1, 0)#MERAMENTE APRA TESTE E ENCONTRAR ALTURA DA MESA
                        
        ###########################################################################################
                            ####        descomentar a baixo para o objeto cair              ######
                self.mesh_copo.objeto.translate(0,-0.1,0) # decrease y-coordinate by 0.01 on each frame
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
                if ( self.score <= 5):
                    #SE TOCAR NO CHAO
                    if self.mesh_copo.objeto.global_position[1] < 0:#decres
                    #olha ta aqui
                            pygame.time.delay(200)# DA DELAY APOS TOCAR NO CHAO
                            self.xrandom = random.uniform(-20 , 20)
                            self.zrandom =random.uniform(0, 10) 
                            self.mesh_copo.objeto.set_position([self.xrandom,15,self.zrandom ] ) #teleport caneca
                            self.camera.set_position([self.xrandom, 3.5,self.zrandom])
                            self.mesh_mesa.objeto.set_position([ random.uniform(-20 , 20),0,  random.uniform(0, 10) ])# teleport mesa
                            if self.count == 0:
                                self.hud_scene.remove(self.allH[0])
                            if self.count == 1:
                                self.hud_scene.remove(self.allH[1])
                            if self.count == 2:
                                self.hud_scene.remove(self.allH[2])
                            self.count+=1
                            self.vidas-=1
                            pygame.mixer.Sound.play(self.gameover)          

                    if self.y_copo == self.y_mesa and self.x_mesa - 7 < self.x_copo < self.x_mesa + 7 and self.z_mesa - 3 < self.z_copo < self.z_mesa + 3:
                            #olha ta aqui
                            pygame.time.delay(200)# DA DELAY APOS TOCAR NO CHAO
                            self.xrandom = random.uniform(-20 , 20)
                            self.zrandom =random.uniform(0, 10) 
                            self.mesh_copo.objeto.set_position([ self.xrandom,15,self.zrandom ] ) #teleport caneca
                            self.camera.set_position([self.xrandom, 3.5,self.zrandom])
                            
                            self.mesh_mesa.objeto.set_position([ random.uniform(-20 , 20),0,  random.uniform(0, 10) ])# teleport mesa
                            self.score +=1
                            self.hud_scene.remove(self.label_1)         
                            self.label_geolocation_1 = RectangleGeometry(width=400, height=80, position=[0, 550], alignment=[0,1])
                            self.label_material_1 = TextureMaterial(TextTexture(text="Score "+ str(self.score),
                                                            system_font_name="Press Start 2P",
                                                            font_size=80, font_color=[0, 0, 0],transparent=True,
                                                            image_width=600, image_height=128,
                                                            align_horizontal=0.5, align_vertical=0.5,
                                                            image_border_width=0))
                            self.label_1 = Mesh(self.label_geolocation_1, self.label_material_1)
                            self.hud_scene.add(self.label_1)
                            pygame.mixer.Sound.play(self.anchivement)        
                # elif ( self.score> 5 and self.score <=10 ):# so apra teste
                elif ( 5 < self.score <= 10 ):
                    self.mesh_chavena.objeto.translate(0,-0.1,0) # decrease y-coordinate by 0.01 on each frame
                    self.x_chavena = self.mesh_chavena.objeto.global_position[0]
                    self.y_chavena = self.mesh_chavena.objeto.global_position[1]
                    self.z_chavena = self.mesh_chavena.objeto.global_position[2]
                    self.y_copo = self.mesh_copo.objeto.global_position[1]
                    self.x_copo = self.mesh_copo.objeto.global_position[0]
                    self.z_copo = self.mesh_copo.objeto.global_position[2]
                    #SE TOCAR NO CHAOs
                    if self.mesh_chavena.objeto.global_position[1] < 0:
                    #olha ta aqui
                            pygame.time.delay(200)# DA DELAY APOS TOCAR NO CHAO
                            self.xrandom = random.uniform(-20 , 20)
                            self.zrandom =random.uniform(0, 10) 
                            self.mesh_chavena.objeto.set_position([self.xrandom,20,self.zrandom ] ) #teleport chavena
                            self.camera.set_position([  self.xrandom , 3.5, self.zrandom])
                            self.mesh_mesa.objeto.set_position([ random.uniform(-20 , 20),0,  random.uniform(0, 10) ])# teleport mesa
                            if self.count == 0:
                                self.hud_scene.remove(self.allH[0])
                            if self.count == 1:
                                self.hud_scene.remove(self.allH[1])
                            if self.count == 2:
                                self.hud_scene.remove(self.allH[2])
                            self.count+=1    
                            self.vidas-=1
                            # if self.vidas == 0:
                            #       self.hud_scene.set_position()          
                            pygame.mixer.Sound.play(self.gameover)   
                    elif self.y_chavena <= self.y_mesa and self.x_mesa - 6 < self.x_chavena < self.x_mesa + 6 and self.z_mesa - 4 < self.z_chavena < self.z_mesa + 4:
                            #olha ta aqui
                            pygame.time.delay(200)# DA DELAY APOS TOCAR NO CHAO
                            self.score+=1
                            print("Score: ", self.c)
                            self.xrandom = random.uniform(-20 , 20)
                            self.zrandom =random.uniform(0, 10) 
                            #olah aqui ta coemntado
                            self.mesh_chavena.objeto.set_position([self.xrandom,15, self.zrandom ] ) #teleport caneca
                            # self.mesh_chavena.objeto.set_position([0,15, 0 ] ) #teleport caneca
                            self.camera.set_position([self.xrandom, 3.5, self.zrandom])
                            # self.mesh_mesa.objeto.set_position([ self.xrandom,0,   self.zrandom ])# teleport mesa
                            self.mesh_mesa.objeto.set_position([random.uniform(-20 , 20),0,  random.uniform(0, 10)  ])# teleport mesa
                            self.hud_scene.remove(self.label_1)        
                            self.label_geolocation_1 = RectangleGeometry(width=400, height=80, position=[0, 550], alignment=[0,1])
                            self.label_material_1 = TextureMaterial(TextTexture(text="Score "+ str(self.score),
                                                            system_font_name="Press Start 2P",
                                                            font_size=80, font_color=[0, 0, 0],transparent=True,
                                                            image_width=600, image_height=128,
                                                            align_horizontal=0.5, align_vertical=0.5,
                                                            image_border_width=0))
                            self.label_1 = Mesh(self.label_geolocation_1, self.label_material_1)
                            self.hud_scene.add(self.label_1)

                            pygame.mixer.Sound.play(self.anchivement)  
                elif ( self.score> 10 ):
                    self.mesh_frigideira.objeto.translate(0,-0.15,0) # decrease y-coordinate by 0.01 on each frame
                    self.x_frigideira = self.mesh_frigideira.objeto.global_position[0]
                    self.y_frigideira = self.mesh_frigideira.objeto.global_position[1]
                    self.z_frigideira = self.mesh_frigideira.objeto.global_position[2]
                    #SE TOCAR NO CHAOs
                    if self.mesh_frigideira.objeto.global_position[1] < 0:
                    #olha ta aqui
                            pygame.time.delay(200)# DA DELAY APOS TOCAR NO CHAO
                            
                            self.xrandom = random.uniform(-20 , 20)
                            self.zrandom =random.uniform(0, 10) 
                            self.mesh_frigideira.objeto.set_position([ self.xrandom,20, self.zrandom ] ) #teleport chavena
                            self.camera.set_position([self.xrandom, 3.5, self.zrandom ])
                            self.mesh_mesa.objeto.set_position([  self.xrandom,0,  self.zrandom ])# teleport mesa
                            if self.count == 0:
                                self.hud_scene.remove(self.allH[0])
                            if self.count == 1:
                                self.hud_scene.remove(self.allH[1])
                            if self.count == 2:
                                self.hud_scene.remove(self.allH[2])
                            self.count+=1
                            self.vidas-=1
                            pygame.mixer.Sound.play(self.gameover)   
                    elif self.y_frigideira <= self.y_mesa and self.x_mesa - 6 < self.x_frigideira < self.x_mesa + 6 and self.z_mesa - 4 < self.z_frigideira < self.z_mesa + 4:
                            #olha ta aqui
                            pygame.time.delay(200)# DA DELAY APOS TOCAR NO CHAO
                            self.score+=1
                            print("Score: ", self.c)
                            self.xrandom = random.uniform(-20 , 20)
                            self.zrandom =random.uniform(0, 10) 
                            #olah aqui ta coemntado
                            # self.mesh_chavena.objeto.set_position([self.xrandom,15, self.zrandom ] ) #teleport caneca
                            self.mesh_frigideira.objeto.set_position([self.xrandom,15, self.zrandom ] ) #teleport caneca
                            self.camera.set_position([self.xrandom, 3.5, self.zrandom ])
                            self.mesh_mesa.objeto.set_position([ random.uniform(-20 , 20),0,   random.uniform(0, 10) ])# teleport mesa
                            # self.mesh_mesa.objeto.set_position([ 0,0,   0 ])# teleport mesa
                            self.hud_scene.remove(self.label_1)        
                            self.label_geolocation_1 = RectangleGeometry(width=400, height=80, position=[0, 550], alignment=[0,1])
                            self.label_material_1 = TextureMaterial(TextTexture(text="Score "+ str(self.score),
                                                            system_font_name="Press Start 2P",
                                                            font_size=80, font_color=[0, 0, 0],transparent=True,
                                                            image_width=600, image_height=128,
                                                            align_horizontal=0.5, align_vertical=0.5,
                                                            image_border_width=0))
                            self.label_1 = Mesh(self.label_geolocation_1, self.label_material_1)
                            self.hud_scene.add(self.label_1)
                            pygame.mixer.Sound.play(self.anchivement)  
            else:
                pygame.mixer.Sound.stop(self.music) 

              
                
              

                self.hud_scene.remove(self.label_1)        
                self.label_geolocation_1 = RectangleGeometry(width=400, height=80, position=[0, 550], alignment=[0,1])
                self.label_material_1 = TextureMaterial(TextTexture(text="bestScore "+ str(self.score),
                                                            system_font_name="Press Start 2P",
                                                            font_size=80, font_color=[0, 0, 0],transparent=True,
                                                            image_width=600, image_height=128,
                                                            align_horizontal=0.5, align_vertical=0.5,
                                                            image_border_width=0))
                self.label_1 = Mesh(self.label_geolocation_1, self.label_material_1)
                self.hud_scene.add(self.label_1)



                self.label_geolocation_6 = RectangleGeometry(width=400, height=80, position=[50, 500], alignment=[0,1])
                self.label_material_6 = TextureMaterial(TextTexture(text="Best score " + str(self.score),
                                            system_font_name="Press Start 2P",
                                            font_size=80, font_color=[0, 0, 0],transparent=True,
                                            image_width=600, image_height=128,
                                            align_horizontal=0.5, align_vertical=0.5,
                                            image_border_width=0))
                self.label_6 = Mesh(self.label_geolocation_6, self.label_material_6)
                self.hud_scene.add(self.label_6)
                
                self.menu_geolocation = RectangleGeometry(width=800, height=600, position=[0, 600], alignment=[0,1])
                self.menu_material = TextureMaterial(Texture("images/lose.png"))
                self.menu_label = Mesh(self.menu_geolocation, self.menu_material)
                
                self.hud_scene.add(self.menu_label)


                              
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(self.hud_scene, self.hud_camera, clear_color=False)


# Instantiate this class and run the program
# Example(screen_size=[900, 800]).run()
Example(screen_size=[800, 600]).run()