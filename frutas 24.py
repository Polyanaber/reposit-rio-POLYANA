# criando uma tupla com alguns elementos
frutas =("maça","banana","cereja")

# Exibindo a tupla
print("Minha tupla de frutas:", frutas)

# Acessando elementos da tupla pelo índice
print("Primeira fruta:", frutas[0]) # índice 0 corresponde a "maça" 
print("segunda fruta:", frutas[1]) # índice 1 corresponde a "banana"
print("terceira fruta:", frutas[2]) # índice 2 corresponde a "cereja"

# Tentando modificar um elemento da tupla (isso gerará um erro)
# frutas[1] = "laranja" # Descomente esta linha para ver o erro

# Descobrindo o tamanho da tupla
print("Número de frutas na tupla:", len(frutas))

#percorrendo a tupla com um loop
print("Listando todas as frutas na tupla:")
for fruta in frutas:
    print(fruta)

# Verificando se um elemento está na tupla
if "banana" in frutas:
    print("Banana está na tupla!")

# criando uma tupla de um único elemento (note a vírgula no final)
unica_fruta = ("melancia",)
print("tupla de um único elemento:", unica_fruta)