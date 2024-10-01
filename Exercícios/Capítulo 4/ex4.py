'''Escreva um programa que peça ao usuário a temperatura atual em graus Celsius. 
Aumente essa temperatura em 2 graus e depois subtraia 5 graus usando os operadores de atribuição adequados. 
Exiba o valor final da temperatura.'''

temperatura = int(input("Digite o valor da temperatura em Celsius: "))

incrementado = temperatura
incrementado += 2

decrementado = temperatura
decrementado -= 5

print("A temperatura aumentada em 2 graus é ", incrementado, " e a temperatura diminuida em 5 graus é ", decrementado)
