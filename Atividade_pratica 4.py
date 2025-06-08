# Leitura do número
numero = input("Digite um número inteiro: ")

# Verificação se é palíndromo
if numero == numero[::-1]:
    print("O número é um palíndromo!")
else:
    print("O número não é um palíndromo.")