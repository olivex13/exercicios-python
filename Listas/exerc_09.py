# 9.	Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor.

print('SOMA DOS QUADRADOS'.center(60))
print('-' * 60)
print('')
vetor = []

for i in range(10):
    numero = int(input('Digite um numero inteiro: '))
    vetor.append(numero)

vetorAoQuadrado = []

for i in vetor:
    aoQuadrado = i ** 2
    vetorAoQuadrado.append(aoQuadrado)

somaDosQuadrados = sum(vetorAoQuadrado)

print(F'Os numeros inteiros digitados foram: {vetor}')
print(f' Os quadrados dos numeros digitados foram: {vetorAoQuadrado}')
print(f' A soma desses numeros é: {somaDosQuadrados}')
