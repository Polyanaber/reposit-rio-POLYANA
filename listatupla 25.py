# Lista para armazenar os nomes cadastrados
cadastros = []

while True:
    print("\n1 - Adicionar nome\n2 - Listar os nomes\n3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")  # Usuário digita o nome
        cadastros.append(nome)  # Nome é adicionado à lista
        print("Nome cadastrado!")

    elif opcao == "2":
        print("\nLista de nomes:")
        for nome in cadastros:  # Exibe todos os nomes cadastrados
            print(nome)
    
    elif opcao == "3":
        print("Saindo do programa...")
        break  # Finaliza o programa

    else:
        print("Opção inválida! Tente novamente.")
