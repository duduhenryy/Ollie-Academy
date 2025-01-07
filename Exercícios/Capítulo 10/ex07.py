try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        resultado = numero1 / numero2
    else:
        raise ValueError("Operação inválida.")

    print(f"Resultado: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
except ZeroDivisionError as e:
    print(f"Erro: {e}")
