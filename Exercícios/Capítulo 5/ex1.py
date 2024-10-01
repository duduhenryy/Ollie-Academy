'''Faça um programa que avalie se um aluno foi aprovado na disciplina ou não, sabendo que as notas variam de 1 a 10 e que a média é 6.'''

nota = int(input("Digite a nota final do aluno: "))

if 0 > nota:
    print("NOTA INVALIDA")
elif nota > 10:
    print("NOTA INVALIDA")
elif nota < 6:
    print("REPROVADO")
else:
    print("APROVADO")
