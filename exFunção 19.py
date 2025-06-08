# Define uma função que calcula a quantidade de dias vividos com base na (idade):
def calcular_dias_de_vida(idade):
  # Calcula e retorna o número aproximado de dias vividos com base na idade (365 dias por ano)
  return idade * 365

# Início do programa principal

# Solicita ao usuário que digite o seu nome
print("Digite o seu nome:")
nome = input()

# Solicita ao usuário que digite a sua idade
print("Digite a sua idade:")
idade = int(input())

# Chama a função para calcular os dias de vida e armazena o resultado na variável 'dias'
dias = calcular_dias_de_vida(idade)

# Exibe uma mensagem com o nome da pessoa e a quantidade de dias vividos
print("Olá", nome + ", você já viveu", dias, "dias.")