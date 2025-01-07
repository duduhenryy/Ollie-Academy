aluno = {"nome": "Maria", "idade": 22, "nota": 8.5}
aluno["curso"] = "Matemática"     # Adiciona o curso
aluno["nota"] = 9.0               # Atualiza a nota
del aluno["idade"]                # Remove a idade
print(aluno)                      # Saída: {'nome': 'Maria', 'nota': 9.0, 'curso': 'Matemática'}
