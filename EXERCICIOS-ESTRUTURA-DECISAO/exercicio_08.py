'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.'''

print('=====QUAL PRODUTO COMPRAR ?====='.center(60))
print("")


produto_1 = float(input('Digite o valor do produto 1: R$ '))
produto_2 = float(input('Digite o valor do produto 2: R$ '))
produto_3 = float(input('Digite o valor do produto 3: R$ '))

if (produto_1 <= produto_2 and produto_1 <= produto_3):
     produto_mais_barato = 'Produto 1'

elif (produto_2 <= produto_1 and produto_2 <= produto_3):
     produto_mais_barato = 'Produto 2'

else:
    produto_mais_barato = 'Produto 3'


print(f'Você deve comprar o produto {produto_mais_barato}, pois é o mais barato.')