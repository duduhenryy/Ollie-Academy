try:
    with open("numeros.txt", "r") as arquivo:
        conteudo = arquivo.readlines()

    if not conteudo:
        raise ValueError("O arquivo está vazio.")

    numeros = [int(linha.strip()) for linha in conteudo]
    soma = sum(numeros)
    print(f"A soma dos números é: {soma}")
except FileNotFoundError:
    print("Erro: O arquivo 'numeros.txt' não foi encontrado.")
except ValueError as e:
    print(f"Erro: {e}")
