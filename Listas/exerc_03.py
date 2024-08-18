# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []

print('MEDIA DE NOTAS'.center(60))
print('-' * 60)
print('')

for i in range(4):
    nota = float(input('Digite as notas: '))
    notas.append(nota)

media = sum(notas) / 4

print(f'A média das notas inseridas é: {media}')
