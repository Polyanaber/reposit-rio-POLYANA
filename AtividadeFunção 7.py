nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:"))
def calcular_dias_de_vida(nome, idade):
    dias = idade * 365
    return nome, dias
nome, dias = calcular_dias_de_vida(nome, idade)
print(f"{nome}, você já viveu aproximadamente {dias} dias.")