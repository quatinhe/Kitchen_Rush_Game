import pygame
import random

# Definir as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definir as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definir a velocidade da bola e da plataforma
BALL_SPEED = 2
ball_speed_x = random.randint(-2, 2)
PLATFORM_SPEED = 5

# Definir o tamanho da bola e da plataforma
BALL_SIZE = 20
PLATFORM_WIDTH = BALL_SIZE * 3
PLATFORM_HEIGHT = BALL_SIZE / 3



# Inicializar o pygame
pygame.init()

# Definir a fonte para o score board
font = pygame.font.Font(None, 36)

# Criar a tela
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Definir a posição inicial da plataforma
platform_x = SCREEN_WIDTH / 2 - PLATFORM_WIDTH / 2
platform_y = SCREEN_HEIGHT - PLATFORM_HEIGHT * 2

# Definir a posição inicial da bola
ball_x = random.randint(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
ball_y = 0 - BALL_SIZE

# Definir a pontuação inicial
score = 0

# Definir o clock para controlar o FPS
clock = pygame.time.Clock()

# Loop principal do jogo
done = False
while not done:

    # Verificar eventos do usuário
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Movimentar a plataforma
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform_x -= PLATFORM_SPEED
    if keys[pygame.K_RIGHT]:
        platform_x += PLATFORM_SPEED

    # Verificar se a plataforma atingiu a borda da tela
    if platform_x < 0:
        platform_x = 0
    elif platform_x > SCREEN_WIDTH - PLATFORM_WIDTH:
        platform_x = SCREEN_WIDTH - PLATFORM_WIDTH

    # Movimentar a bola
    ball_y += BALL_SPEED

    # Verificar se a bola atingiu a plataforma
    if ball_y + BALL_SIZE >= platform_y and ball_x + BALL_SIZE > platform_x and ball_x < platform_x + PLATFORM_WIDTH:
        score += 1
        BALL_SPEED += 0.1
        ball_y = platform_y - BALL_SIZE
        BALL_SPEED *= -1

    # Verificar se a bola caiu na tela
    elif ball_y > SCREEN_HEIGHT:
        score -= 1
        ball_x = random.randint(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
        ball_y = 0 - BALL_SIZE
        BALL_SPEED = 2

    # Desenhar a tela
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT])
    pygame.draw.circle(screen, RED, [ball_x, ball_y], BALL_SIZE)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [10, 10])
    pygame.display.flip()

    # Controlar o FPS
    clock.tick(60)

# Fechar o pygame
pygame.quit()