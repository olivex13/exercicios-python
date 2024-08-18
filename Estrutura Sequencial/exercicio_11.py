#	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#  a.	Para homens: (72.7*h) - 58
#  b.	Para mulheres: (62.1*h) - 44.7

print('Calculadora de peso ideal'.center(60))
sexo = None
altura = None
peso_ideal = None

menu = """
[1] MULHER
[2] HOMEM
"""
print(menu)
opcao_escolhida = int(input('Digite a opção desejada: '))

if opcao_escolhida == 2:
    altura = float(input('Digite sua altura: '))
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {peso_ideal:.2f}')
elif opcao_escolhida == 1:
    altura = float(input('Digite sua altura: '))
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {peso_ideal:.2f}')
else:
    print('Digite uma opção valida')
