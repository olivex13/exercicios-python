'''10.	Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!" conforme o caso.'''

print('PERIODO DE ESTUDOS'.center(60))
print('')

menu = """ Qual periodo você estuda? \n
[M] Matutino
[V] Vespertino
[N] Noturno \n
"""

print(menu)

opcao_escolhida = input('Digite a opção desejada: ')
opcao_escolhida = opcao_escolhida.lower()

if (opcao_escolhida == "m"):
    print('Bom dia!!')
elif (opcao_escolhida == "v"):
    print('Boa tarde!')
elif (opcao_escolhida == "n"):
    print('Boa noite!!')
else:
    print('Digite uma opção válida.')
