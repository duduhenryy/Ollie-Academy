import csv

with open("produtos.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        quantidade = int(linha['Quantidade'])
        preco = float(linha['Preço'])
        valor_total = quantidade * preco
        print(f"Produto: {linha['Produto']}, Valor Total: R$ {valor_total:.2f}")
