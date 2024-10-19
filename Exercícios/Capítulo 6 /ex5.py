# Utilize o loop while e escreva um programa que continue pedindo números ao usuário até que ele digite um número negativo, 
# momento em que o programa deve terminar.

# Use while para continuar pedindo números até o usuário digitar um número negativo
numero = 0
while numero >= 0:
    numero = int(input("Digite um número (negativo para sair): "))
    if numero >= 0:
        print(f"Você digitou {numero}.")
print("Programa encerrado.")
