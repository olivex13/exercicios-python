# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e 
# calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá 
# 3pagar. Imprima os dados do programa com as mensagens adequadas.

print('==========CALCULADORA DE TRIBUTOS DO JOAO PAPO DE PESCADOR========== \n' )

ALIQUOTA_MULTA = 4

quilo_pescado = float(input('Digite a quantidade de quilos pescados: '))
print('')

if (quilo_pescado > 50):
    quilo_excedente = quilo_pescado - 50
    valor_da_multa = quilo_excedente * ALIQUOTA_MULTA
    print(f' Você excedeu {quilo_excedente} kilos, o valor de multa a pagar é: R$ {valor_da_multa:.2f}')

else:
    print('Você não excedeu o limite permitido.')
    
print('')