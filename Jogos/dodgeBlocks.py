import pygame
import random
import sys

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Dodge the Blocks")

BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# jogador
player_x, player_y = 400, 500
player_velocidade = 10
player_tamanho = 50

# blocos
bloco_largura, bloco_altura = 50, 50
bloco_x = random.randint(0, largura - bloco_largura)
bloco_y = -50
bloco_velocidade = 7

# loop principal
relogio = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # movimentar o jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and player_x > 0:
        player_x -= player_velocidade
    if teclas[pygame.K_RIGHT] and player_x < largura - player_tamanho:
        player_x += player_velocidade

    # atualizar posição do bloco
    bloco_y += bloco_velocidade
    if bloco_y > altura:
        bloco_y = -50
        bloco_x = random.randint(0, largura - bloco_largura)

    # detectar colisão
    if (player_x < bloco_x + bloco_largura and player_x + player_tamanho > bloco_x and
        player_y < bloco_y + bloco_altura and player_y + player_tamanho > bloco_y):
        print("Você perdeu!")
        pygame.quit()
        sys.exit()

    # desenhar na tela
    tela.fill(BRANCO)
    pygame.draw.rect(tela, VERMELHO, (player_x, player_y, player_tamanho, player_tamanho))
    pygame.draw.rect(tela, AZUL, (bloco_x, bloco_y, bloco_largura, bloco_altura))
    pygame.display.flip()

    # controlar fps
    relogio.tick(30)
