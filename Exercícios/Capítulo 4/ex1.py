'''Crie um programa que receba um número do usuário e printe false quando o número for par e true quando ímpar.
   Resolução:'''

numero = int(input("Digite um número: "))
impar = (numero % 2) != 0

print("O número é ímpar? ", impar)
