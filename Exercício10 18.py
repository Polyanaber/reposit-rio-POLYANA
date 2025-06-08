# Pede um número ao usuário e converte para número inteiro
numero = int(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#"Esse código pede pro usuário digitar um número e diz se ele é positivo,
#  negativo ou zero. Ele usa input pra pegar o número, e depois usa if,
#  elif e else pra fazer a comparação. Se for maior que zero,
#  ele fala que é positivo; se for menor, fala que é negativo;
#  e se for igual a zero, ele diz que é zero."