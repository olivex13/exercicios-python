# 2.	Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista1 = []

print('LENDO NUMEROS REAIS'.center(60))
print('-' * 60)
print('')

for i in range(10):
    real = float(input('Digite um numero real: '))
    lista1.append(real)

print('')

print('MOSTRANDO OS NUMEROS DIGITADOS'.center(60))
print('-' * 60)
print('')


for i in lista1[::-1]:
    print(i)    

