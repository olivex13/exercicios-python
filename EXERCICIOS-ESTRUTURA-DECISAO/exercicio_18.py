#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print('==========VERIFICAÇÃO DE DATAS=========='.center(120))
print('')


data = input('Digite uma data no formato DD/MM/AAAA: ')

def validar_data (data):
    dia, mes, ano = map(int, data.split('/'))
    if 1 <= mes <= 12 and 1 <= dia <= 31:
        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 29:
                    return False
            elif dia > 28:
                return False
        elif mes in [4, 6, 9, 11] and dia > 30:
            return False
        return True
    else:
        return False
    
if validar_data(data):
    print('A data é valida')
else:
    print('A data é invalida')




