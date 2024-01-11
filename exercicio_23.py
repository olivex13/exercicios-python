'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.'''

print('==========INTEIRO OU DECIMAL?=========='.center(120))
print('')

def verificar_numero (numero):
    if numero == round(numero):
        return 'Inteiro'
    else:
        return 'Decimal'
    
numero = float(input("Digite um numero: "))
verificacao = verificar_numero(numero)


print(f'O numero digitado é {verificacao}')