# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
print('CALCULANDO Á AREA DE UM CIRCULO'.center(60))
print('')
raio = int(input('Digite o valor do Raio: '))
PI = 3.14159
area = PI * (raio ** 2)
print(f'O valor da áreado circulo é de: {area:.2f}')