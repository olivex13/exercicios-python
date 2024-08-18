#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#-	                      Até 5 Kg           Acima de 5 Kg
#-	   Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#-	   Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

print('<==========FRUTERIA DO PYTHON==========>'.center(60))
print('')

def preco_morango(kg): 
    if (kg <= 5):
        return 2.50
    else:
        return 2.20
    
def preco_maca(kg): 
    if (kg <= 5):
        return 1.80
    else:
        return 1.20

kg_morango = float(input('Digite quantos KG de Morango deseja comprar: '))
kg_maca = float(input('Digite quantos KG de maçã deseja comprar: '))

preco_do_morango = preco_morango(kg_morango)
preco_da_maca = preco_maca(kg_maca)

total_do_morango = preco_do_morango * kg_morango
total_da_maca = preco_da_maca * kg_maca
total_kg = kg_morango + kg_maca
compra_bruta = total_da_maca + total_do_morango

def valor_total(kg_total, compra_bruta):
    if (kg_total > 8 or compra_bruta > 25):
        desconto = compra_bruta * 0.10
        total = compra_bruta - desconto
        return total
    
total_da_compra = valor_total(total_kg, compra_bruta)

print(f'Você está comprando {kg_morango:.0f} kilos de morango, {kg_maca:.0f} kilos de maçã \n O valor total da compra ficou em R$ {compra_bruta:.2f} \n E com desconto ficou R$ {total_da_compra:.2f}')