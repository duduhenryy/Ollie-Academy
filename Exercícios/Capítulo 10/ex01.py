try:
    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))
    resultado = numerador / denominador
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
else:
    print(f"Resultado: {resultado:.2f}")
