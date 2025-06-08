# Inicializar uma lista de listas chamada MATRIZ para representar a matriz 4x4
# Cada lista interna representa uma linha da matriz, inicializada com 4 zeros.
MATRIZ = [[0] * 4 for _ in range(4)]

# Preenche a linha de índice 0 da matriz:
# Atribui o valor 0 ao elemento na linha 0, coluna 0
MATRIZ[0][0] = 0
# Atribui o valor 1 ao elemento na linha 0, coluna 1
MATRIZ[0][1] = 1
# Atribui o valor 0 ao elemento na linha 0, coluna 2
MATRIZ[0][2] = 0
# Atribui o valor 1 ao elemento na linha 0, coluna 3
MATRIZ[0][3] = 1

# Preenche a linha de índice 1 da matriz:
# Atribui o valor 0 ao elemento na linha 1, coluna 0
MATRIZ[1][0] = 0
# Atribui o valor 0 ao elemento na linha 1, coluna 1
MATRIZ[1][1] = 0
# Atribui o valor 1 ao elemento na linha 1, coluna 2
MATRIZ[1][2] = 1
# Atribui o valor 0 ao elemento na linha 1, coluna 3
MATRIZ[1][3] = 0

# Exibindo os valores da linha 0 da matriz:
# Imprime um cabeçalho indicando a linha que será exibida
print("linha 0:")
# Loop que itera pelos índices das colunas (de 0 a 3)
for contador1 in range(4):
    # Imprime o elemento da linha 0 na coluna atual do loop
    print(MATRIZ[0][contador1])

# Exibindo os valores da linha 1 da matriz:
# Imprime uma linha em branco e um cabeçalho para próxima linha
print("\nlinha 1:")
# Loop que itera pelos índices das colunas (de 0 a 3)
for contador1 in range(4):
    # Imprime o elemento da linha 1 na coluna atual do loop
    print(MATRIZ[1][contador1])

# Exibindo os valores da matriz:
# Loop externo para percorrer os índices das linhas (de 0 a 3)
for contador1 in range(4):
    # Loop interno para percorrer os índices das colunas (de 0 a 3)
    for contador2 in range(4):
        # Imprime o elemento da matriz na linha e coluna atuais, sem adicionar uma nova linha
        print(MATRIZ[contador1][contador2], end=" ")
    # Imprime uma nova linha após a impressão de todos os elementos de uma linha da matriz
    print()