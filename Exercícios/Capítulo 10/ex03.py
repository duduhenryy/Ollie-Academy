import math

try:
    numero = float(input("Digite um número: "))
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz:.2f}")
except ValueError as e:
    print(f"Erro: {e}")
