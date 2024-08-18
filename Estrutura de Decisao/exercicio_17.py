'''Faça um Programa que peça um número correspondente a um determinado ano 
em seguida informe se este ano é ou não bissexto.'''

print('==========ANO BISSEXTO=========='.center(60))
print('')

def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return 'É bissexto'
    else:
        return 'não é bissexto'
    
ano = int(input('Digite o ano: '))
bissexto = eh_bissexto(ano)

print(f'O ano {ano}, {bissexto}')
