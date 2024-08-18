# 1.	Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista1 = []

print('LENDO NUMEROS INTEIROS'.center(60))
print('-' * 60)
print('')

for i in range(5):
    inteiro = int(input('Digite um numero inteiro: '))
    lista1.append(inteiro)

print('')

print('MOSTRANDO OS NUMEROS DIGITADOS'.center(60))
print('-' * 60)
print('')


for i in lista1:
    print(i)    

