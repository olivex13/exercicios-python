#5.	Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

print('DEFININDO NUMEROS PARES E IMPARES'.center(60))
print('-' * 60)

numeros_inteiros = []
numeros_pares = []
numeros_impares = []

for i in range(20):
    numero = int(input('Digite um numero inteiro: '))
    numeros_inteiros.append(numero)

for i in numeros_inteiros:
    if i % 2 == 0:
        numeros_pares.append(i)
    else:
        numeros_impares.append(i)

print('')
print(f'Os numero inteiros digitados são: {numeros_inteiros}')
print(f'Os numeros pares digitados foram: {numeros_pares}')
print(f'Os numeros impares digitados foram: {numeros_impares}')