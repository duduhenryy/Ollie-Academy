import csv

dados = [
    {"Nome": "Ana", "Idade": 20, "Nota": 8.5},
    {"Nome": "Pedro", "Idade": 22, "Nota": 7.0},
    {"Nome": "Carla", "Idade": 19, "Nota": 9.2}
]

with open("alunos.csv", "w", newline="") as arquivo:
    campos = ["Nome", "Idade", "Nota"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()  # Escreve os cabeçalhos
    escritor.writerows(dados)  # Escreve os dados
