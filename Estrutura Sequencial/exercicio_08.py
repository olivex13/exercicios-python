#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
horas_trabalhadas = None
valor_da_hora = None 

print('Calculadora de salário'.center(60))
print('')
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
valor_da_hora = float(input('Digite o valor da hora trabalhada: '))

valor_salario = horas_trabalhadas * valor_da_hora

print(f'O valor do salário é R$ {valor_salario:.2f}')