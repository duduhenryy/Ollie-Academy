precos = {"maçã": 2.50, "banana": 1.20, "laranja": 3.00}
item = input("Qual item você deseja verificar? ")

if item in precos:
    print(f"O preço de {item} é R$ {precos[item]:.2f}")
else:
    print("Item não disponível.")
# Exemplo de entrada e saída:
# Entrada: "banana"
# Saída: "O preço de banana é R$ 1.20"
