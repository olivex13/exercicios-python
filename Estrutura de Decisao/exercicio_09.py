#9.	Faça um Programa que leia três números e mostre-os em ordem decrescente.

print('COLOCANDO NUMEROS EM ORDEM DESCRESCENTE'.center(60))
print('')

def ordem_decrescente(num1, num2, num3):
    lista_numeros= [num1, num2, num3]
    lista_numeros.sort(reverse=True)
    return lista_numeros

numero_1 = float(input('Digite o primeiro numero: '))
numero_2 = float(input('Digite o segundo numero: '))
numero_3 = float(input('Digite o terceiro numero: '))

numeros_ordenados = ordem_decrescente(numero_1, numero_2, numero_3)

print(f'Segue os numeros ordenados, {numeros_ordenados}')