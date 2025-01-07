texto = "banana"
contador = {}

for letra in texto:
    contador[letra] = contador.get(letra, 0) + 1

print(contador)                   # Saída: {'b': 1, 'a': 3, 'n': 2}
