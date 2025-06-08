MATRIZ = [[0] * 4 for_in range(4)]

for contador1 in range(4):

    for contador2 in range(4):

        valor_digitado = int(input(f"Digite o {numero}ºnúmero: "))
        
        MATRIZ[contador1][contador2] = valor_digitado

        numero += 1

    print()

for contador1 in range(4):
