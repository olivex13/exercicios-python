#  2.	Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print('MOSTRANDO NUMEROS POSITIVOS E NEGATIVOS'.center(120))
print('')

numero_digitado = float(input('Digite um numero: '))

if (numero_digitado >= 0):
    print('O numero é positivo')
else:
    print('O numero é negativo.')
