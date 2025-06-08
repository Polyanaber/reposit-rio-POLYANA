# Este programa compara três números e irá mostrar
# qual é maior, o menor e a média desses números.

num1 = int (input("DIGITE O PRIMEIRO NÚMERO: "))
num2 = int (input("DIGITE O SEGUNDO NÚMERO: "))
num3 = int (input("DIGITE O TERCEIRO NÚMERO: "))

# Verificar qual é o maoir número
if (num1 > num2) and (num1 > num3):
     maior = num1

elif (num2 > num1) and (num2 > num3):
     maior = num2

else:
     maior = num3

# Verificar qual é o menor número

if (num1 < num2) and (num1 < num3):
     menor = num1

elif (num2 < num1) and (num2 < num3):
     menor = num2

else:
     menor = num3

# Calcula a média dos três números

     media = (num1 + num2 + num3) / 3

 # Exibe os Resultados

print ("\n----------------RESULTADO---------------------")
print (f"O MAOIR NÚMERO É: {maior}")
print (f"O MENOR NÚMERO É: {menor}")
print (f"A MÉDIA DOS NÚMEROS É: {media:6,1f}")


print ("-------------------------------------")