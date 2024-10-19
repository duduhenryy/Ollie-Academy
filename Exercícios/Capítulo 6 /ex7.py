# DESAFIO: Crie um jogo simples em que o programa gera um número aleatório entre 1 e 10, e o usuário tem que adivinhar. 
# O programa deve continuar pedindo palpites até o usuário acertar.

import random

numero_secreto = random.randint(1, 10)
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
print("Parabéns! Você acertou.")

