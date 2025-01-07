lista = ["Python", "Java", "C++", "JavaScript"]

try:
    indice = int(input("Digite um índice (0 a 3): "))
    print(f"O valor no índice {indice} é {lista[indice]}")
except IndexError:
    print("Erro: O índice está fora do intervalo da lista.")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
