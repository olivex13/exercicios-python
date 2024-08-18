# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print('CALCULANDO A AREA DE UM QUADRADO'.center(60))
print('')

lado_quadrado = float(input('Digite a medida do lateral do quadrado: '))
area_do_quadrado = lado_quadrado ** 2
dobro_quadrado = area_do_quadrado * 2

print(f'A area do quadrado é: {area_do_quadrado} e o seu dobro é: {dobro_quadrado}')