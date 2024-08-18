# Faça um Programa que leia três números e mostre o maior e o menor deles.

print('ENCONTRE O MENOR NUMERO'.center(60))
print('')

def encontrar_menor_numero (numbr1, numbr2, numbr3):
    if (numbr1 <= numbr2 and numbr1 <= numbr3):
        return numbr1
    elif (numbr2 <= numbr1 and numbr2 <= numbr3):
        return numbr2
    else:
        return numbr3
    

numero_1 = float(input('Digite o primeiro numero: '))
numero_2 = float(input('Digite o segundo numero: '))
numero_3 = float(input('Digite o terceiro numero: '))

menor_numero = encontrar_menor_numero(numero_1, numero_2, numero_3)

print("")
print(f'O menor numero digitado é: {menor_numero:.0f}')