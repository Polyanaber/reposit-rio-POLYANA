# Inicializar uma lista de listas chamada MATRIZ para representar a matriz 4x4
# Cada lista interna representa uma linha da matriz, inicializada com 4 zeros.
MATRIZ = [[0] * 4 for _ in range(4)]

# Preenchendo a matriz com dados informados pelo usuário
# Loop externo para percorrer as linhas (de índice 0 a 3)
for linha in range(4):
    # Loop interno para percorrer as colunas (de índice 0 a 3)
    for coluna in range(4):
        # Solicita ao usuário um valor para a posição específica da matriz
        print(f"Digite o valor para a posição MATRIZ[{linha}][{coluna}]:")
        # Converte o valor digitado para inteiro e armazena na posição correta
        MATRIZ[linha][coluna] = int(input())

# Exibindo os valores da matriz:
# Loop externo para percorrer os índices das linhas (de 0 a 3)
for contador1 in range(4):
    # Loop interno para percorrer os índices das colunas (de 0 a 3)
    for contador2 in range(4):
        # Imprime o elemento da matriz na linha e coluna atuais, sem adicionar nova linha
        print(MATRIZ[contador1][contador2], end=" ")
    # Imprime uma nova linha após imprimir todos os elementos de uma linha
    print()