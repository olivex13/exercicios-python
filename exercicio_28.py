#28.	O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#	                      Até 5 Kg           Acima de 5 Kg
#   	File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#   	Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#   	Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente 
#receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
#comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, 
#tipo de pagamento, valor do desconto e valor a pagar.

print('==========HIPERMERCADO TABAJARA=========='.center(120))

def file_duplo(kg): 
    if (kg <= 5):
        return 4.90
    else:
        return 5.80
    
def alcatra(kg): 
    if (kg <= 5):
        return 5.90
    else:
        return 6.80

def picanha(kg): 
    if (kg <= 5):
        return 6.90
    else:
        return 7.80
    
kg_alcatra = float(input('Digite quantos KG de Alcatra deseja comprar: '))
kg_file_duplo = float(input('Digite quantos KG de File Duplo deseja comprar: '))
kg_picanha = float(input('Digite quantos KG de Picanha deseja comprar: '))

preco_da_picanha = picanha(kg_picanha)
preco_da_alcatra = alcatra(kg_alcatra)
preco_file_duplo = file_duplo(kg_file_duplo)

total_da_picanha = preco_da_picanha * kg_picanha
total_da_alcatra = preco_da_alcatra * kg_alcatra
total_file_duplo = preco_file_duplo * kg_file_duplo
total_kg = kg_picanha + kg_file_duplo + kg_alcatra
compra_bruta = total_da_picanha + total_da_alcatra + total_file_duplo

forma_de_pagamento = int(input(""" Digite a forma de pagamento: \n
                               [1] CARTÃO TABAJARA
                               [2] PIX
                               [3] DINHEIRO
                               [4] DEBITO 
                               
                               Selecione uma opção: => """))

def forma_pagamento(forma_de_pagamento, compra_bruta):
    if (forma_de_pagamento  == 1):
        desconto = compra_bruta * 0.05
        total = compra_bruta - desconto
        return total
    
total_da_compra = forma_pagamento(forma_de_pagamento, compra_bruta)

print(F""" ====================CUPOM FISCAL TABAJARA====================\n
       {kg_alcatra:.0f}kg ALCATRA    R$ {total_da_alcatra:.2f}
       {kg_picanha:.0f}kg PICANHA    R$ {total_da_picanha:.2f}
       {kg_file_duplo:.0f}kg FILE DUPLO R$ {total_file_duplo:.2f}


    TOTAL R$  {compra_bruta}          TOTAL COM DESCONTO R$ {total_da_compra:.2f}
    ===========================================================
                            VOLTE SEMPRE""")