def classifica_aluno(nota):
    if nota < 0 or nota > 10:
        return "Nota inválida"
    elif nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota >= 5:
        return "Regular"
    else:
        return "Insuficiente"

nota_aluno = float(input("Digite a nota do aluno: "))
classificacao = classifica_aluno(nota_aluno)
print("A classificação do aluno é:", classificacao)
