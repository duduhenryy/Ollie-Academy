'''Você foi contratado pelo Governo para criar um software de um radar de trânsito que ficará na rodovia de Cascavel - PR.
O radar deve receber uma velocidade e, com base no valor, determinará se o veículo está respeitando o limite de velocidade de 80 km/h.
Se o veículo estiver respeitando o valor de 80, o radar deve imprimir a mensagem de aceitação. Caso o veículo esteja acima desse limite,
o radar automaticamente deve imprimir uma mensagem de multa e retornar o valor dessa infração com base no valor da porcentagem de
excesso de velocidade atribuído ao valor padrão da multa de 120 reais.
Ex: se o veículo estiver a 100km/h, o valor da multa deverá ser computado como o valor padrão incrementado com o valor baseado na
 porcentagem de excesso, ou seja, de 20km/h.
'''

velocidade = int(input("Digite o valor da velocidade do veículo: "))

valor_multa = (120*velocidade)/80
infracao = valor_multa - 120

if velocidade < 0:
    print("NÃO EXISTE VELOCIDADE NEGATIVA")
elif velocidade > 0 and velocidade <= 80:
    print("O veículo está respeitando o limite de velocidade.")
else:
    print("MULTA: o valor da infracao para a velocidade de ", velocidade, "km/h foi de" , infracao, "reais e o valor da multa é ", valor_multa , " reais")
