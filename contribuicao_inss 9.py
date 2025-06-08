salario_contribuicao = float(input("Digite o seu salário"))

if salario_contribuicao <= 1692.72:

         contribuicao_inss = salario_contribuicao * 0.08

elif salario_contribuicao >= 1692.73 and salario_contribuicao <= 2822.90:
        
        contribuicao_inss = salario_contribuicao * 0.09

elif salario_contribuicao >= 2822.90 and salario_contribuicao <= 5645.90:
        
        contribuicao_inss = salario_contribuicao * 0.11

salario_liquido = salario_contribuicao - contribuicao_inss

print (f"A Contribuição do INSS: R$ {contribuicao_inss:.2f}")
print (f"O Salário bruto é: {salario_contribuicao:.2f}")
print (f"O Salário líquido é: {salario_liquido:.2f}")