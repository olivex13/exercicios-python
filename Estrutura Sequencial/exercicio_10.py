#	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A - o produto do dobro do primeiro com metade do segundo .
# B - a soma do triplo do primeiro com o terceiro.
# C - o terceiro elevado ao cubo.

print('==========MINI CALCULADORA==========')
number_1 = int(input('Digite um numero inteiro: '))
number_2 = int(input('Digite outro numero inteiro: '))
number_3 = float(input('Digite um numero real: '))

variavel_a = (number_1 * 2) + (number_2 / 2)
variavel_b = (number_1 * 3) + number_3
variavel_c = number_3 ** 2

print (f"""
    A - o produto do dobro do primeiro com metade do segundo é equivalente á {variavel_a}
    \n
    B - a soma do triplo do primeiro com o terceiro é equivalente á {variavel_b}
    \n
    C - o terceiro elevado ao cubo é equivalente á {variavel_c}
    \n
      """)