'''Peça dois números ao usuário e printe se o segundo número é divisível pelo primeiro.
   Resolução:'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

divisivel = numero2 % numero1 == 0

print(numero2, "é divisivel por", numero1, "?", divisivel)
