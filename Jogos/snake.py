import pygame
import random
import sys

# inicializar o Pygame
pygame.init()

# configurações do jogo
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()

# definição de cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

# configurações da cobrinha
tamanho_bloco = 20
velocidade = 15

# fonte para pontuação
fonte = pygame.font.SysFont("arial", 35)

# exibir a pontuação
def mostrar_pontuacao(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, [10, 10])


def jogo():
    # posições iniciais da cobra
    pos_x = largura // 2
    pos_y = altura // 2

    # movimento inicial
    movimento_x = 0
    movimento_y = 0

    # corpo da cobra (lista de blocos)
    corpo_cobra = []
    comprimento_cobra = 1

    # posição inicial da fruta
    fruta_x = random.randint(0, (largura // tamanho_bloco) - 1) * tamanho_bloco
    fruta_y = random.randint(0, (altura // tamanho_bloco) - 1) * tamanho_bloco

    # pontuação
    pontos = 0

    # loop principal do jogo
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # detectar teclas pressionadas
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and movimento_y == 0:
                    movimento_x = 0
                    movimento_y = -tamanho_bloco
                if evento.key == pygame.K_DOWN and movimento_y == 0:
                    movimento_x = 0
                    movimento_y = tamanho_bloco
                if evento.key == pygame.K_LEFT and movimento_x == 0:
                    movimento_x = -tamanho_bloco
                    movimento_y = 0
                if evento.key == pygame.K_RIGHT and movimento_x == 0:
                    movimento_x = tamanho_bloco
                    movimento_y = 0

        # atualizar posição da cobra
        pos_x += movimento_x
        pos_y += movimento_y

        # detectar colisão com as bordas
        if pos_x < 0 or pos_x >= largura or pos_y < 0 or pos_y >= altura:
            print("Game Over! Você bateu na parede.")
            pygame.quit()
            sys.exit()

        # atualizar a cobra
        bloco_cabeca = [pos_x, pos_y]
        corpo_cobra.append(bloco_cabeca)
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        # detectar colisão com o próprio corpo
        for bloco in corpo_cobra[:-1]:
            if bloco == bloco_cabeca:
                print("Game Over! Você bateu no próprio corpo.")
                pygame.quit()
                sys.exit()

        # detectar colisão com a fruta
        if pos_x == fruta_x and pos_y == fruta_y:
            fruta_x = random.randint(0, (largura // tamanho_bloco) - 1) * tamanho_bloco
            fruta_y = random.randint(0, (altura // tamanho_bloco) - 1) * tamanho_bloco
            comprimento_cobra += 1
            pontos += 10

        # desenhar na tela
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [fruta_x, fruta_y, tamanho_bloco, tamanho_bloco])  # Fruta
        for bloco in corpo_cobra:
            pygame.draw.rect(tela, VERDE, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])  # Cobra

        # exibir pontuação
        mostrar_pontuacao(pontos)

        pygame.display.update()
        relogio.tick(velocidade)

# iniciar o jogo
jogo()
