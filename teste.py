import random
import pygame

# Definição de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 30
PLATFORM_WIDTH = BALL_SIZE * 3
PLATFORM_HEIGHT = 10
PLATFORM_SPEED = 2
SCORE_FONT_SIZE = 30
SCORE_POS = (10, 10)
MAX_BOUNCES = 1

# Inicialização do Pygame
pygame.init()

# Configuração da janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da esfera")

# Configuração da fonte para exibir a pontuação
score_font = pygame.font.Font(None, SCORE_FONT_SIZE)

# Configuração da plataforma
platform_x = SCREEN_WIDTH / 2 - PLATFORM_WIDTH / 2
platform_y = SCREEN_HEIGHT - PLATFORM_HEIGHT * 2
platform_rect = pygame.Rect(platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

# Configuração da esfera
ball_x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
ball_y = 0
ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)
ball_speed = 1

# Variáveis do jogo
score = 0
game_over = False
num_bounces = 0

# Loop principal do jogo
while not game_over:
    # Manipulação de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Movimentação da plataforma
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform_rect.x -= PLATFORM_SPEED
    elif keys[pygame.K_RIGHT]:
        platform_rect.x += PLATFORM_SPEED

    # Limitação da plataforma aos limites da tela
    if platform_rect.right > SCREEN_WIDTH:
        platform_rect.right = SCREEN_WIDTH
    elif platform_rect.left < 0:
        platform_rect.left = 0

    # Movimentação da esfera
    ball_rect.y += ball_speed

    # Verificação de colisão da esfera com a plataforma
    if ball_rect.colliderect(platform_rect) and ball_speed > 0:
        ball_rect.bottom = platform_rect.top
        ball_speed = -10
        num_bounces += 1
        score += 1

    # Verificação de colisão da esfera com o chão
    if ball_rect.bottom > SCREEN_HEIGHT:
        ball_rect.x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
        ball_rect.y = 0
        ball_speed = 1
        num_bounces = 0
        score -= 1

        # Verificação do fim do jogo
        if score == 0 or num_bounces >= MAX_BOUNCES:
            game_over = True

    # Limpeza da tela
    screen.fill((255, 255, 255))

    # Desenho da plataforma
    pygame.draw.rect(screen, (0, 0, 0) ,  platform_rect)

    # Desenho da esfera
    pygame.draw.circle(screen, (255, 0, 0), ball_rect.center, BALL_SIZE // 2)

    # Exibição da pontuação
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, SCORE_POS)

    # Atualização da tela
    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()