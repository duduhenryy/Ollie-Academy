'''Faça um programa que avalie se um número é positivo, negativo ou zero e escreva na tela a resposta.'''

numero = int(input("Digite o valor: "))

if numero < 0:
    print("Negativo")
elif numero == 0:
    print("Nulo (0)")
else:
    print("Positivo")
