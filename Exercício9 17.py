# Passo 1: Perguntar a idade
idade = int(input("Qual a sua idade? "))  # o input recebe uma string, o int() converte pra número

# Passo 2: Verificar se pode dirigir
if idade >= 18:
    print("Você pode dirigir!")
else:
    print("Você ainda não pode dirigir.")


# Explicação
#"Oi pessoal, eu fiz um código simples em Python que serve
# pra verificar se uma pessoa já tem idade suficiente pra dirigir.
# Primeiro, o programa pergunta qual é a sua idade,
# usando o comando input. Como o que a gente digita vem como texto,
# eu uso int() pra transformar isso em número. 
# Depois, o programa faz uma verificação com if.
# Ele checa se a idade é maior ou igual a 18 anos. Se for,
# ele mostra na tela que a pessoa pode dirigir. Mas se não for,
# ele mostra que ainda não pode dirigir.
# É um código simples, mas já usa conceitos importantes como entrada de dados, 
# conversão de tipos e estrutura condicional."