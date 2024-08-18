# 4.	Faça um Programa que leia um vetor de 10 caracteres
#  e diga quantas consoantes foram lidas. Imprima as consoantes.


print('LENDO CARACTERES'.center(60))
print('-' * 60)

vetor = []

for i in range(10):
    caractere = input(f'Digite o caractere {i+1}: ')
    while len(caractere) != 1:
        print('Digite apenas um caractere. ')
        caractere = input(f'Digite o caractere {i+1}: ')
    vetor.append(caractere)

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []

for i in vetor:
    if i not in vogais:
        consoantes.append(i)

quantidade = len(consoantes)

print('')
print(f'A quantidade de consoantes digitadas é: {quantidade}' )
print('')
print(f'As consoantes digitadas foram: ')
print(consoantes) 