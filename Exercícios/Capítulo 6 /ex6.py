# Escreva um programa que peça ao usuário um nome de usuário e senha. Dê ao usuário 3 tentativas para acertar o login.
# Após 3 tentativas erradas, exiba uma mensagem de erro e termine o programa.

usuario_correto = "admin"
senha_correta = 1234
palpites = 0

while palpites < 3:
    nome = input("Digite o nome de usuário: ")
    senha = int(input("Digite a senha: "))

    if nome == usuario_correto and senha == senha_correta:
        print("Parabéns!!! Você acertou!")
        break
    else:
        palpites += 1
        print("Usuário ou senha incorretos! Tente novamente.")

if palpites == 3:
    print("Fim das tentativas.")
