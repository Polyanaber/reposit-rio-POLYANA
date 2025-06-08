# Definindo a função 'VerificarSexo' que recebe a variavel 'Sexo'
# como parâmetro
def verificarSexo(sexo):
    # Verificar se o sexo é "f" para feminino
    if sexo == "f":
    # Se for feminino, imprime "Feminino"
       print("Feminino")
    else:
    # Caso contrário, imprime "Masculino"
       print("Masculino")

# Solicita ao usuário para digitar o seu sexo (f para feminino e m para 
# masculino)
print("Digite o seu sexo: (f) para feminino e (m) para masculino:")

#Lê a entrada do usuário e armazena na variável 'sexo'
sexo = input()

# Chama a função 'verificar' passando o valor de 'sexo'
verificarSexo(sexo)