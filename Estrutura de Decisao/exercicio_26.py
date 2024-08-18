#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a.	Álcool:	até 20 litros, desconto de 3% por litro //	acima de 20 litros, desconto de 5% por litro
# d.	Gasolina: até 20 litros, desconto de 4% por litro // acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina)
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 
# o preço do litro do álcool é R$ 1,90.
print('<==========POSTO DE COMBUSTÍVEL PYTHON==========>'.center(60))
print('')

PRECO_LITRO_GASOLINA = 2.50
PRECO_LITRO_ALCOOL = 1.90

def alcool (PRECO_LITRO_ALCOOL, qnt_alcool):
    if (qnt_alcool <= 20):
        desconto = PRECO_LITRO_ALCOOL * 0.03
        return PRECO_LITRO_ALCOOL - desconto
    else: 
        desconto = PRECO_LITRO_ALCOOL * 0.05
        return PRECO_LITRO_ALCOOL - desconto
    
def gasolina (PRECO_LITRO_GASOLINA, qnt_gasolina):
    if (qnt_gasolina <= 20):
        desconto = PRECO_LITRO_GASOLINA * 0.04
        return PRECO_LITRO_GASOLINA - desconto
    else: 
        desconto = PRECO_LITRO_GASOLINA * 0.6
        return PRECO_LITRO_GASOLINA - desconto

main = str(input(""" Qual Combustivel deseja abastecer?
                [A] Alcool
                [G] Gasolina
                 --> """
        )).lower()

qnt_litros = float(input('Quanto litros deseja abastecer? '))

if (main == 'a'):
    preco_combustivel = alcool(PRECO_LITRO_ALCOOL, qnt_litros)
    total = preco_combustivel * qnt_litros
    combustivel_selecionado = 'Alcool'

elif (main == 'g'):
    preco_combustivel = gasolina(PRECO_LITRO_GASOLINA, qnt_litros)
    total = preco_combustivel * qnt_litros
    combustivel_selecionado = 'Gasolina'

else:
    print('Digite uma opção válida.')

print(f' Você está abastecendo {qnt_litros} litros de {combustivel_selecionado} e o valor total a pagar ficou R$ {total:.2f}')