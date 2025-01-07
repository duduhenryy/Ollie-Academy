def divide_e_resto(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto

resultado = divide_e_resto(17, 5)
print(resultado)                  # Saída: (3, 2)
