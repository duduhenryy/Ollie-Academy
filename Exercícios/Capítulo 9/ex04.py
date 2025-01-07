import csv

novos_produtos = [
    ["Leite", 10, 4.00],
    ["Café", 6, 12.50]
]

with open("produtos.csv", "a", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(novos_produtos)
