#Crie um programa que peça um número de 1 a 10 ao usuário e exiba a tabuada de multiplicação desse número.

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
