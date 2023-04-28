import pygame
from pygame.locals import *

# Inicializando o Pygame
pygame.init()

# Inicializando o clock
clock = pygame.time.Clock()

# Definindo constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
AVATAR_SIZE = (128, 128)  # Aumentando o tamanho do sprite
AVATAR_SPEED = 3
BACKGROUND_COLOR = (0, 0, 255)  # Definindo uma cor de fundo
OBJECTIVE_SIZE = (30, 30)
OBJECTIVE_COLOR = (255, 0, 0)

# Configurando a janela do Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo 2D")

# Carregando o Pokémon
avatar = pygame.image.load('pokemon.png').convert_alpha()  # Convertendo o PNG para melhorar a transparência
avatar = pygame.transform.scale(avatar, AVATAR_SIZE)
avatar_rect = avatar.get_rect()
avatar_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Definindo a posição do objetivo
objective_x = 100
objective_y = 100

# Loop principal do jogo
while True:
    # Lidando com eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    # Limpando a tela
    screen.fill(BACKGROUND_COLOR)  # Preenchendo a tela com uma cor de fundo

    # Desenhando o avatar
    screen.blit(avatar, avatar_rect)

    # Lidando com a lógica de movimento do avatar
    keys = pygame.key.get_pressed()
    avatar_rect.x += (keys[K_RIGHT] - keys[K_LEFT]) * AVATAR_SPEED
    avatar_rect.y += (keys[K_DOWN] - keys[K_UP]) * AVATAR_SPEED
    avatar_rect.clamp_ip(screen.get_rect())

    # Desenhando o objetivo
    pygame.draw.rect(screen, OBJECTIVE_COLOR, (objective_x, objective_y, *OBJECTIVE_SIZE))

    # Lidando com a lógica de colisão entre o avatar e o objetivo
    if avatar_rect.colliderect(pygame.Rect(objective_x, objective_y, *OBJECTIVE_SIZE)):
        print("Você encontrou o objetivo!")
        objective_x = 500
        objective_y = 300

    # Limitando a taxa de atualização de frames por segundo
    clock.tick(60)  # Define a taxa de atualização para 60 FPS

    # Atualizando a tela
    pygame.display.update()
