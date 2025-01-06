def somar_intervalo(valor1, valor2):
    if valor1 > valor2:
        return "O valor1 é maior que o valor2."
    elif valor1 == valor2:
        return "O valor1 é igual ao valor2."
    
    resultado = 0
    for _ in range(valor2-valor1+1):
        resultado += valor1
        valor1 += 1
        
    return resultado

loop = True

while loop:
    
    valor1 = int(input("Digite o valor1: "))
    valor2 = int(input("Digite o valor2: "))
    
    resultado = somar_intervalo(valor1, valor2)
    print(resultado)
    if type(resultado) == int:
        loop = False
