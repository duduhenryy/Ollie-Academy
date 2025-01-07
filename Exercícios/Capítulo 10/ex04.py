def verificar_idade(idades):
    for idade in idades:
        if idade < 18:
            raise ValueError(f"Idade inválida: {idade}. É necessário ser maior de 18 anos.")

try:
    idades = [20, 17, 25, 15]
    verificar_idade(idades)
except ValueError as e:
    print(f"Erro: {e}")
