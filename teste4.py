import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def cubo_em_cima_da_mesa(posicao_cubo, dimensoes_mesa):
    cubo_x, cubo_y, cubo_z = posicao_cubo
    mesa_largura, mesa_comprimento, mesa_altura = dimensoes_mesa

    if (cubo_x >= 0 and cubo_x <= mesa_largura) and (cubo_y >= 0 and cubo_y <= mesa_comprimento) and cubo_z <= mesa_altura:
        return True
    else:
        return False

def desenhar_mesa(dimensoes_mesa):
    mesa_largura, mesa_comprimento, mesa_altura = dimensoes_mesa

    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)  # Cor da mesa
    glVertex3f(0, 0, 0)
    glVertex3f(0, mesa_comprimento, 0)
    glVertex3f(mesa_largura, mesa_comprimento, 0)
    glVertex3f(mesa_largura, 0, 0)
    glEnd()

def desenhar_cubo(posicao_cubo):
    cubo_x, cubo_y, cubo_z = posicao_cubo

    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Cor do cubo
    glVertex3f(cubo_x - 1, cubo_y - 1, cubo_z - 1)
    glVertex3f(cubo_x - 1, cubo_y + 1, cubo_z - 1)
    glVertex3f(cubo_x + 1, cubo_y + 1, cubo_z - 1)
    glVertex3f(cubo_x + 1, cubo_y - 1, cubo_z - 1)

    glVertex3f(cubo_x - 1, cubo_y - 1, cubo_z + 1)
    glVertex3f(cubo_x - 1, cubo_y + 1, cubo_z + 1)
    glVertex3f(cubo_x + 1, cubo_y + 1, cubo_z + 1)
    glVertex3f(cubo_x + 1, cubo_y - 1, cubo_z + 1)

    glVertex3f(cubo_x - 1, cubo_y - 1, cubo_z - 1)
    glVertex3f(cubo_x - 1, cubo_y + 1, cubo_z - 1)
    glVertex3f(cubo_x - 1, cubo_y + 1, cubo_z + 1)
    glVertex3f(cubo_x - 1, cubo_y - 1, cubo_z + 1)

    glVertex3f(cubo_x + 1, cubo_y - 1, cubo_z - 1)
    glVertex3f(cubo_x + 1, cubo_y + 1, cubo_z - 1)
    glVertex3f(cubo_x + 1, cubo_y + 1, cubo_z + 1)
    glVertex3f(cubo_x + 1, cubo_y - 1, cubo_z + 1)

    glVertex3f(cubo_x - 1, cubo_y - 1, cubo_z - 1)
    glVertex3f(cubo_x + 1, cubo_y - 1, cubo_z - 1)
    glVertex3f(cubo_x + 1, cubo_y - 1, cubo_z + 1)
    glVertex3f(cubo_x - 1, cubo_y - 1, cubo_z + 1)

    glVertex3f(cubo_x - 1, cubo_y + 1, cubo_z - 1)
    glVertex3f(cubo_x + 1, cubo_y + 1, cubo_z - 1)
    glVertex3f(cubo_x + 1, cubo_y + 1, cubo_z + 1)
    glVertex3f(cubo_x - 1, cubo_y + 1, cubo_z + 1)
    glEnd()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), OPENGL | DOUBLEBUF)
    pygame.display.set_caption('Cubo em cima da mesa')
    clock = pygame.time.Clock()

    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    posicao_cubo = [0, 0, 2]  # Posição inicial do cubo
    dimensoes_mesa = [20, 30, 5]  # Dimensões da mesa

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        desenhar_mesa(dimensoes_mesa)
        desenhar_cubo(posicao_cubo)

        pygame.display.flip()
        clock.tick(60)

        if cubo_em_cima_da_mesa(posicao_cubo, dimensoes_mesa):
            print("O cubo está em cima da mesa.")
        else:
            print("O cubo não está em cima da mesa.")

if __name__ == '__main__':
    main()