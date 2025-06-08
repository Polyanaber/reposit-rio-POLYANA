# Inicializamos listas com zeros para definir o tamanho.
NOME = [0] * 3
IDADE = [0] * 3
TELEFONE = [0] * 3
BAIRRO = [0] * 3
MUNICIPIO = [0] * 3
ESTADO = [0] * 3
RUA = [0] * 3
NUMERO = [0] * 3  # nova lista para o número da casa
# A variável 'cont' é usada como índice para percorrer as listas.
cont = 0
# Loop 'for' em Python que intera de 0 até 2 (inclusive).
for cont in range(3): 
    #imprime o cabeçalho do cadatro, incrementando 'cont' para exibir o número dp cadastro.
    print(f"----- {cont + 1}º-CADASTRO -----")
    print()
    # Solocita e lê o nome do usuário, armazenando-o na lista NOME na posição 'cont'.
    print("Digite o seu nome:")
    NOME[cont] = input()
    # Solicita e lê a idade do usuário, convertendo a entrada para inteiro e armazenando na lista IDADE
    print("Digite sua idade:")
    IDADE[cont] = int(input())
    # Solicita e lê o telefone do usuário, armazenando-o
    # Simula a limpeza da tela.
    print("Digite seu numero de telefone:")
    TELEFONE[cont] = int(input())
    # Solicita e lê o bairro
    print("Digite o nome do seu bairro:")
    BAIRRO[cont] = input()
    # Solicita e lê o município
    print("Digite o nome do seu município:")
    MUNICIPIO[cont] = input()
    # Solicita e lê o estado
    print("Digite o nome do seu estado:")
    ESTADO[cont] = input()
    # Solicita e lê a rua do usúario, armazenando-o na lista RUA na posição 'cont'
    print("Digite o nome da sua Rua:")
    RUA[cont] = input()
    # Solicita e lê o número da casa, armazenando-o na lista NUMERO
    print("Digite o número da sua casa:")
    NUMERO[cont] = int(input())

print("\n" * 20)
# Ouro loop 'for' para exibir os dados cadastrados.
for cont in range(3):
    #imprime os dados de cada pessoa formatados.
    print(f"NOME: {NOME[cont]}")
    print(f"IDADE: {IDADE[cont]} anos")
    print(f"TELEFONE: {TELEFONE[cont]}")
    print(f"ENDEREÇO: Rua {RUA[cont]}, Nº {NUMERO[cont]} - Bairro {BAIRRO[cont]}, {MUNICIPIO[cont]} - {ESTADO[cont]}")
    print("-----------------------------")