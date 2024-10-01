'''Peça dois números ao usuário e printe se o segundo número é divisível pelo primeiro.'''

primeiro_numero = int(input("Digite o primeiro valor: "))
segundo_numero = int(input("Digite o segundo valor: "))

if primeiro_numero % segundo_numero == 0:
    print("é divisivel")
else:
    print("não é divisível")
