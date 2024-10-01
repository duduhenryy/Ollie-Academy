'''Faça um programa que calcule o desconto em uma loja com base no preço do produto. E printe na tela o valor com o desconto aplicado.
Comprou mais de 100 R$ → 5% de desconto.
Comprou mais de 300 R$ → 10% de desconto.
Comprou mais de 1000 R$ → 15% de desconto.
'''

preco = int(input("Digite o preço do produto: "))
desconto = 0
valor_final = 0

if preco < 0:
    print("PREÇO INVALIDO!")
elif preco > 0 and preco <= 100:
    print("Não há desconto! O valor a ser pago é: ", preco)
elif preco > 100 and preco <= 300:
    desconto = preco*0.05
    valor_final = preco - desconto
    print("O valor do produto é ", preco, ", o valor do desconto de 5% é ", desconto, "e o valor final é ", valor_final)
elif preco > 300 and preco <= 1000:
    desconto = preco*0.1
    valor_final = preco - desconto
    print("O valor do produto é ", preco, ", o valor do desconto de 10% é ", desconto, "e o valor final é ", valor_final)
elif preco > 1000:
    desconto = preco*0.15
    valor_final = preco - desconto
    print("O valor do produto é ", preco, ", o valor do desconto de 15% é ", desconto, "e o valor final é ", valor_final)
