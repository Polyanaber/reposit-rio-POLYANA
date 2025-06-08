# Criando um procedimento com parâmetro
# (em python, definimos uma função que aceita um argumento)
def saudacao(nomeUsuario):

    print(f"Olá {nomeUsuario}")

# Escreval ("Digite o seu nome: ")
print("Digite o seu nome: ")

# Lendo o nome do usuário
nome = input()

# saudacao(nome)  //chamando um procedimento
#                 // e passando parâmetro
saudacao(nome)