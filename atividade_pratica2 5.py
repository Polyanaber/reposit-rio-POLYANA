print(" SEJA BEM-VINDO(A) AO CONVERSOR DE TEMPERATURA!")

def trocatemp(a,b,c):
    return a * b + c

print("Digite a temperatura em graus celcius que voce queira transformar em fahrenheit: ")

valor1 = int(input())
valor2 = 1.8
valor3 = 32

resultado = trocatemp(valor1, valor2, valor3)
print(f"O resultado da conversão foi: {resultado} Graus Fahrenheit!")