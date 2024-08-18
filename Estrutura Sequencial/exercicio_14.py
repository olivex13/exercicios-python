# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# a tinta é vendida em latas de 18 litros que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

 # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
 # comprar apenas latas de 18 litros;
 # comprar apenas galões de 3,6 litros;
 # misturar latas e galões, de forma que o desperdício de tinta seja menor.  
 # Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

print('==========LOJA DE TINTAS - CALCULADORA==========')
print('')

COBERTURA_TINTA = 6 #cada 1 litros de tinta, cobre 6m² 


def calcular_tinta (tamanho_area, COBERTURA_TINTA):
    quantidade_tinta = tamanho_area * 1.1 / COBERTURA_TINTA
    return quantidade_tinta

def calcular_latas_18(quantidade_tinta):
    volume_da_lata_18  = 18
    latas_necessarias_18 = math.ceil(quantidade_tinta / volume_da_lata_18)
    return latas_necessarias_18

def calcular_latas_3(quantidade_tinta):
    volume_da_lata_3 = 3.6
    latas_necessarias_3 = math.ceil(quantidade_tinta / volume_da_lata_3)
    return latas_necessarias_3


tamanho_area = float(input('Digite a área a ser pintada em m²: '))
print("")

quantidade_tinta = calcular_tinta (tamanho_area, COBERTURA_TINTA)
latas_18_necessarias = calcular_latas_18(quantidade_tinta)
latas_3_necessarias = calcular_latas_3(quantidade_tinta)

VALOR_LATA_18 =  80
VALOR_LATA_3 = 25
custo_tinta_18 = latas_18_necessarias * VALOR_LATA_18
custo_tinta_3 = latas_3_necessarias * VALOR_LATA_3

print(f'Você vai precisar de {latas_18_necessarias} Latas de 18 litros e isso vai custar R$ {custo_tinta_18:.2f}')
print(f'Ou você pode comprar {latas_3_necessarias} Latas de 3.6 litros que vai custar R$ {custo_tinta_3:.2f}')
print('')

if (custo_tinta_18 > custo_tinta_3):
    print(f'É melhor comprar {latas_3_necessarias} latas de tintas de 3.6L, vai sair mais barato!')

else:
    print(f'É melhor comprar {latas_18_necessarias} latas de tintas de 18L, vai sair mais barato!30')