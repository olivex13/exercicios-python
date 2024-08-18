# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#o	C = 5 * ((F-32) / 9).

print('==========CONVERSOR DE TEMPERATURA==========')
graus_fahrenheit = float(input('Digite a temperatura em grau Farenheit: '))
graus_celsius = 5 * ((graus_fahrenheit - 32) / 9)

print(f' A temperatura {graus_fahrenheit}ºf é equivalente a temperatura {graus_celsius}ºC')