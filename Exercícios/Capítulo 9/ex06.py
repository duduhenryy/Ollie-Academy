import csv

with open("alunos.csv", "r") as entrada, open("aprovados.csv", "w", newline="") as saida:
    leitor = csv.DictReader(entrada)
    campos = ["Nome", "Idade", "Nota"]
    escritor = csv.DictWriter(saida, fieldnames=campos)

    escritor.writeheader()  # Escreve os cabeçalhos
    for linha in leitor:
        if float(linha["Nota"]) >= 8.0:
            escritor.writerow(linha)
