# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a.	salário bruto.
# b.	quanto pagou ao INSS.
# c.	quanto pagou ao sindicato.
# d.	o salário líquido.
# e.	calcule os descontos e o salário líquido, conforme a tabela abaixo:
#       + Salário Bruto : R$
#       - IR (11%) : R$
#       - INSS (8%) : R$
#       - Sindicato ( 5%) : R$
#       = Salário Liquido : R$
#     Obs.: Salário Bruto - Descontos = Salário Líquido.


print('============CALCULADORA SALARIO============')
print('')

salario_bruto = None
valor_hora = None
horas_trabalhadas = None


valor_hora = float(input('Digite o valor recebido por hora: '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
salario_bruto = horas_trabalhadas * valor_hora

inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = horas_trabalhadas * 0.5
salario_liquido = salario_bruto - (inss + ir + sindicato)

print('==========Demonstrativo de salario==========')

print (f"""
+ Salario Bruto: R$ {salario_bruto:.2f}
- IR: R$ {ir:.2f}
- INSS: R$ {inss:.2f}
- SINDICATO: R$ {sindicato:.2f}
= SALARIO LIQUIDO: R$ {salario_liquido:.2f}

""")