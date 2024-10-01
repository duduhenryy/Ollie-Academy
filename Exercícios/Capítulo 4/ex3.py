''' Escreva um código que peça ao usuário dois números e, em seguida, adicione o segundo número ao primeiro três vezes consecutivas, 
    usando o operador de atribuição adequado. Exiba o valor final.

Resolução: '''

primeiro_termo = int(input("Digite o primeiro termo: "))
segundo_termo = int(input("Digite o segundo termo: "))

primeiro_termo += segundo_termo
primeiro_termo += segundo_termo
primeiro_termo += segundo_termo

print("O valor final é: ", primeiro_termo)
