'''Crie um programa que receba um número do usuário e printe ‘False’ quando o número for par e ‘True’ quando ímpar.'''

valor = int(input("Digite o valor que deseja saber se é par ou impar: "))

if valor % 2 == 0:
    print("O numero é par.")
else:
    print("O número é ímpar.")
