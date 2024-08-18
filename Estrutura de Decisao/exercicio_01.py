# 1.	Faça um Programa que peça dois números e imprima o maior deles.

print('MOSTRANDO O MAIOR NUMERO'.center(60))

numero_a = float(input('Digite o primeiro numero: '))
numero_b = float (input('Digite o segundo numero: '))

if (numero_a > numero_b):
    print(f' Maior numero é {numero_a}')
elif (numero_b > numero_a):
    print (f'O maior numero é: {numero_b}')
else: 
    print ('Os numeros digitados são iguais.')