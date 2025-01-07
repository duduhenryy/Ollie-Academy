import csv

with open("produtos.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"Produto: {linha['Produto']}, Quantidade: {linha['Quantidade']}, Preço: {linha['Preço']}")
