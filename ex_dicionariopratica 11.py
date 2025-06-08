#Dicionário para armazenar os alunos e suas ídades
alunos = {}

# Lista de nomes predefinidos
nomes = ["Ana", "Carlos", "Bianca", "Felipe",]

# Pergunta a idade de cada aluno e salva no dicionário
for nome in nomes:
    idade = input(f"Digite a idade de {nome}: ") # Entrada de idade 
    alunos[nome] = idade # Adiciona ao dicionário

# Exibe a lista de alunos com suas idades:
print("\nLista de alunos:")
for nome, idade in alunos.items():
    print(f"{nome}: {idade} anos")