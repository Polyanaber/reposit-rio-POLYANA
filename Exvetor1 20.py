# Em Python, usamos listas para simular vetores.
# Criamos umas lista do tamanho 4. Os elementos serão strings
vetorDeCaracter = [None] * 4 # Inicializa a lista com 4 elementos 'Nome'

# Atribui a struing "Erick" à primeira posição da lista (índice 0).
vetorDeCaracter[0] = "Erick"

# A função 'print' em Python é equivalente a 'escreval' do Visualg.
# Usamos f-strings para formatar a saída, inserindo o valor da variável.
print(f"Na posição 0, o valor é.: {vetorDeCaracter[0]}")