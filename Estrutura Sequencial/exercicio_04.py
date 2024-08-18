# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('Calculadora de notas'.center(60))
print('')
bimestre_1 = float(input('Digite a nota do primeiro Bimestre: '))
bimestre_2 = float(input('Digite a nota do segundo Bimestre: '))
bimestre_3 = float(input('Digite a nota do terceiro Bimestre: '))
bimestre_4 = float(input('Digite a nota do quarto Bimestre: '))

media = (bimestre_1 + bimestre_2 + bimestre_3 + bimestre_4) / 4

if media >= 6:
    print(f'Sua média é {media:.2f} e você foi aprovado!')
else:
    print(f'Sua média é {media:.2f} e você foi reprovado!')