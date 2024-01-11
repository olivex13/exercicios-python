'''13.	Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

print('=====DIAS DA SEMANA====='.center(60))
print('')

def dias_da_semana(dia):
    while True:
        if (dia == 1):
            return 'Domingo'
        elif (dia == 2):
            return 'Segunda'
        elif (dia == 3):
            return 'Terça'
        elif (dia == 4):
            return 'Quarta'
        elif (dia == 5):
            return 'Quinta'
        elif (dia == 6):
            return 'Sexta'
        elif (dia == 7):
            return 'Sabado'
        else:
            print('Digite uma opção valida')
            return None
        
menu = ("""Selecione um dia da semana: 
        [1] Domingo
        [2] Segunda
        [3] Terça
        [4] Quarta
        [5] Quinta
        [6] Sexta
        [7] Sabado
      """)

while True:

    print(menu)
    opcao_escolhida = int(input('Digite a opção desejada: '))

    dia_da_semana = dias_da_semana(opcao_escolhida)

    if (dia_da_semana is not None):
        print (f'O dia escolhido foi {dia_da_semana}')
        break