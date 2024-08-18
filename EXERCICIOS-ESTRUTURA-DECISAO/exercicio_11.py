'''11.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
	Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
	salários até R$ 280,00 (incluindo) : aumento de 20%
	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
	salários de R$ 1500,00 em diante : aumento de 5% 

 ======= Após o aumento ser realizado, informe na tela: ======
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

print('=====AUMENTO DE SALARIO====='.center(60))
print('')

def aumento_salario_20 (salario):
    aumento = salario * 0.20
    novo_salario = salario + aumento
    return novo_salario

def aumento_salario_15 (salario):
    aumento = salario * 0.15
    novo_salario = salario + aumento
    return novo_salario

def aumento_salario_10 (salario):
    aumento = salario * 0.10
    novo_salario = salario + aumento
    return novo_salario

def aumento_salario_5 (salario):
    aumento = salario * 0.05
    novo_salario = salario + aumento
    return novo_salario

salario_atual = float(input('Digite o salario_atual: '))

if (salario_atual <= 280):
    salario_com_aumento = aumento_salario_20(salario_atual)
    valor_aumento = salario_com_aumento - salario_atual
    percentual = '20 %'
    print(f"""
          O salario antes do reajuste era R$ {salario_atual:.2f}.
          O percentual de aumento foi: {percentual}
          Teve um aumento de R$ {valor_aumento:.2f} 
          Depois do reajuste o salário ficou R$ {salario_com_aumento:.2f}""")

elif (salario_atual > 280 and salario_atual <= 700):
    salario_com_aumento = aumento_salario_15(salario_atual)
    valor_aumento = salario_com_aumento - salario_atual
    percentual = '15 %'
    print(f"""
          O salario antes do reajuste era R$ {salario_atual:.2f}.
          O percentual de aumento foi: {percentual}
          Teve um aumento de R$ {valor_aumento:.2f} 
          Depois do reajuste o salário ficou R$ {salario_com_aumento:.2f}""")

elif (salario_atual > 700 and salario_atual <= 1500):
    salario_com_aumento = aumento_salario_10(salario_atual)
    valor_aumento = salario_com_aumento - salario_atual
    percentual = '10 %'
    print(f"""
          O salario antes do reajuste era R$ {salario_atual:.2f}.
          O percentual de aumento foi: {percentual}
          Teve um aumento de R$ {valor_aumento:.2f} 
          Depois do reajuste o salário ficou R$ {salario_com_aumento:.2f}""")

elif (salario_atual > 1500):
    salario_com_aumento = aumento_salario_5(salario_atual)
    valor_aumento = salario_com_aumento - salario_atual
    percentual = '5 %'
    print(f"""
          O salario antes do reajuste era R$ {salario_atual:.2f}.
          O percentual de aumento foi: {percentual}
          Teve um aumento de R$ {valor_aumento:.2f} 
          Depois do reajuste o salário ficou R$ {salario_com_aumento:.2f}""")
