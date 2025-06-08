print (" CARDÁPIO: ")

print ("PIZZARIA BOM DA VIDA - BEM VINDO")
print ("___PREÇOS___")
print (" ")
print ("*****PIZZAS - SABORES*****")
print (" TRADICIONAIS ")

print ("CALABRESA")
print ("Molho de tomate, mussarela, calabresa, cebola e orégano")

print ("FRANGO")
print ("Molho de tomate, mussarela, frango, , cebola e orégano")

print ("CATUPIRY")
print ("Molho de tomate, mussarela, presento, ovo, catupiry, bacon, cebola e orégano")

print ("*****PIZZAS - TAMANHO*****")
print (" Pizza pequena    R$ 10,00")
print (" Pizza Média      R$ 15,00")
print ("Pizza Grande      R$ 20,00")
print ("*****REFRIGERANTES*****")
print ("Coca-Cola       R$ 7,00")
print ("Guaraná         R$ 6,00")
print ("Fanta           R$ 5,00")
print ("_______________________")
print (" ")
print ("FAÇA O SEU PEDIDO PARA PIZZA:")
print ("1 - CALABREZA")
print ("2 - FRANGO")
print ("3 - CATUPIRY")
print ("_____________________________")

# Lê a escolha do sabor da pizza do usuário e converte para inteiro
pedidopizza = int(input())

print ("DIGITE O TAMANHO DA PIZZA:")
print ("P - PEQUENA")
print ("M - MÉDIA")
print ("G - GRANDE")
print ("__________________________")
# Lê a escolha do tamanho da pizza do usuário e converte para inteiro
tampizza = input(). upper()

print ("FAÇA O SEU PEDIDO PARA REFRIGERANTE")
print ("1 - COCA-COLA")
print ("2 - GUARANÁ")
print ("3 - FANTA")
print ("___________________________________")
#  Lê a escolha do refrigerante do usuário e converte para inteiro
pedidorefri = int(input())


# Cacular o preço total e descreve o pedido utilizando elif com parênteses.
if (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.00 + 6.00
    pedidos = "CALABREZA, PEQUENA, GUARANÁ"

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00
    pedidos = "CALABREZA, PEQUENA, COCA-COLA"

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 10.00 + 5.00
    pedidos = "CALABREZA, PEQUENA, FANTA"

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00
    pedidos = "CALABREZA, MÉDIA, COCA-COLA"

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.00 + 6.00
    pedidos = "CALABREZA, MÉDIA, GUARANÁ"

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.00 + 5.00
    pedidos = "CALABREZA, MÉDIA, FANTA"

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.00 + 7.00
    pedidos = "CALABREZA, GRANDE, COCA-COLA"

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.00 + 5.00
    pedidos = "CALABREZA, GRANDE, FANTA"

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.00 + 6.00
    pedidos = "CALABREZA, GRANDE, GUARANÁ"

elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.00 + 6.00
    pedidos = "FRANGO, PEQUENA, GUARANÁ"

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00
    pedidos = "FRANGO, PEQUENA, COCA-COLA"

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 10.00 + 5.00
    pedidos = "FRANGO, PEQUENA, FANTA"

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00
    pedidos = "FRANGO, MÉDIA, COCA-COLA"

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.00 + 6.00
    pedidos = "FRANGO, MÉDIA, GUARANÁ"

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.00 + 5.00
    pedidos = "FRANGO, MÉDIA, FANTA"

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.00 + 7.00
    pedidos = "FRANGO, GRANDE, COCA-COLA"

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.00 + 5.00
    pedidos = "FRANGO, GRANDE, FANTA"

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.00 + 6.00
    pedidos = "FRANGO, GRANDE, GUARANÁ"

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.00 + 6.00
    pedidos = "CATUPIRY, PEQUENA, GUARANÁ"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00
    pedidos = "CATUPIRY, PEQUENA, COCA-COLA"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 10.00 + 5.00
    pedidos = "CATUPIRY, PEQUENA, FANTA"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00
    pedidos = "CATUPIRY, MÉDIA, COCA-COLA"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.00 + 6.00
    pedidos = "CATUPIRY, MÉDIA, GUARANÁ"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.00 + 5.00
    pedidos = "CATUPIRY, MÉDIA, FANTA"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.00 + 7.00
    pedidos = "CATUPIRY, GRANDE, COCA-COLA"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.00 + 5.00
    pedidos = "CATUPIRY, GRANDE, FANTA"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.00 + 6.00
    pedidos = "CATUPIRY, GRANDE, GUARANÁ"
else :
    precopagar = 0.0
    pedidos = "PEDIDO INVÁLIDO"

# Exibe o resumo do pedido e o preço total a pagar
print ("_______________________________________")
print (f"O TOTAL A PAGAR É: R$ {precopagar:.2f}")
print ("_______________________________________")
print (f"OS PEDIDOS FORAM {pedidos}")
print ("_______________________________________")
print ("BOM APETITE E SEJA BEM VINDO")