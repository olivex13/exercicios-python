# 16.	Utilize uma lista para resolver o problema a seguir. 
# Uma empresa paga seus vendedores com base em comissões. 
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas de $3000 
# em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) que determine quantos vendedores 
# receberam salários nos seguintes intervalos de valores:
#- a.	$200 - $299
#- b.	$300 - $399
#- c.	$400 - $499
#- d.	$500 - $599
#- e.	$600 - $699
#- f.	$700 - $799
#- g.	$800 - $899
#- h.	$900 - $999
#- i.	$1000 em diante

#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, 
#sem fazer vários ifs aninhados.

print('Pagamento dos vendedores'.center(60))
print('-' * 60)
print('')

contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
salarioFixo = 200
intervalos = [
    "$200 - $299",
    "$300 - $399",
    "$400 - $499",
    "$500 - $599",
    "$600 - $699",
    "$700 - $799",
    "$800 - $899",
    "$900 - $999",
    "$1000 ou mais"
]

vendasBrutas = []
contadorLoop = 1 

print('Digite as vendas brutas dos vendedores ou Digite -1 para sair. \n')

while True:
    venda = float(input(f'Digite o valor da vendas Brutas do vendedor {contadorLoop}: '))
    if venda == -1:
        break
    else:
        vendasBrutas.append(venda)
        contadorLoop += 1

salarioTotal = []

for vendaBruta in vendasBrutas:
    salario = salarioFixo + (vendaBruta * 0.09)
    salarioTotal.append(salario)
  
    if salario >= 1000:
        indice = 8  
    else:
        indice = int((salario - salarioFixo) // 100)

        contadores[indice] += 1


print('\nResultados:')
for i in range(len(contadores)):    
    print(f"{intervalos[i]}: {contadores[i]} vendedor(es)")

print('')
print('Salário dos Vendedores: \n')
contSalario = 1

for i in salarioTotal:
    print(f'O vendedor {contSalario} ganhou ${i}.')
    contSalario += 1