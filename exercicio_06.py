# Faça um Programa que leia três números e mostre o maior deles.

print('ENCONTRE O MAIOR NUMERO'.center(60))
print("")
def encontrar_maior_numero (numbr1, numbr2, numbr3):
    if (numbr1 >= numbr2 and numbr1 >= numbr3):
        return numbr1
    elif (numbr2 >= numbr1 and numbr2 >= numbr3):
        return numbr2
    else:
        return numbr3
    
numero_1 = float(input('Digite o primeiro numero: '))
numero_2 = float(input('Digite o segundo numero: '))    
numero_3 = float(input('Digite o terceiro numero: '))

maior_numero = encontrar_maior_numero(numero_1, numero_2, numero_3)

print('')
print(f'O maior numero digitado é: {maior_numero:.0f}')