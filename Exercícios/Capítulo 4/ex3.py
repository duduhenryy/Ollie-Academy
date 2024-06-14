''' PA1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    PA2 = [5, 3, 1, -1, -3, -5, -7, -9, -11, -13]
    PA3 = [20, 24, 28, 32, 36, 40, 44, 48, 52, 56]

Usando como teste as três PA’s a cima para teste, crie um programa que peça ao usuário a posição do termo que ele deseja
descobrir e os dois primeiros termos de uma PA de primeira ordem qualquer e printe na tela o termo que o usuário 
escolheu descobrir.

Ex:
Se  o usuário escolher o termo na posição 10 e em seguida informar que os dois primeiros termos são 1 e 4 em sequência,
o programa deve printar 28 como o décimo termo.

Resolução: '''

posicao = int(input("Digite o termo que deseja descobrir: "))
primeiro_termo = int(input("Digite o primeiro termo: "))
segundo_termo = int(input("Digite o segundo termo: "))

razao = segundo_termo - primeiro_termo

decimo_termo = primeiro_termo + (posicao - 1) * razao

print("O décimo termo da progressão aritmética é:", decimo_termo)
