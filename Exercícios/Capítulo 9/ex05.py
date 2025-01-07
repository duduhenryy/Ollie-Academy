import csv

with open("alunos.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    total_notas = 0
    maior_nota = 0
    aluno_maior_nota = ""
    count = 0

    for linha in leitor:
        nota = float(linha["Nota"])
        total_notas += nota
        count += 1
        if nota > maior_nota:
            maior_nota = nota
            aluno_maior_nota = linha["Nome"]

    media = total_notas / count
    print(f"Média das Notas: {media:.2f}")
    print(f"Aluno com a Maior Nota: {aluno_maior_nota} ({maior_nota:.2f})")
