'''12.	Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda
que depende do salário bruto (conforme tabela abaixo) 
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita)

 O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
 O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
	Desconto do IR:
	Salário Bruto até 900 (inclusive) - isento
	Salário Bruto até 1500 (inclusive) - desconto de 5%
	Salário Bruto até 2500 (inclusive) - desconto de 10%
	Salário Bruto acima de 2500 - desconto de 20% 

======Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.======
-    	Salário Bruto: (5 * 220)        : R$ 1100,00
-	     (-) IR (5%)                     : R$   55,00  
-	     (-) INSS ( 10%)                 : R$  110,00
-	        FGTS (11%)                      : R$  121,00
-	        Total de descontos              : R$  165,00
-          Salário Liquido                 : R$  935,00 '''

print('=====FOLHA DE PAGAMENTO====='.center(60))
print('')

def calculo_salario_bruto(horas, valor_hora):
    salario_bruto = horas * valor_hora
    return salario_bruto

def desconto_ir(salario_bruto):
    if (salario_bruto <= 900):
        ir = 0
        return ir
    
    elif (salario_bruto >= 901 and salario_bruto <= 1500):
        ir = salario_bruto * 0.05
        return ir
    
    elif (salario_bruto >= 1501 and salario_bruto <= 2500):
        ir = salario_bruto * 0.10
        return ir
    
    elif (salario_bruto >= 2501):
        ir = salario_bruto * 0.20
        return ir

def desconto_sindicato(salario_bruto):
    sindicato = salario_bruto * 0.03
    return sindicato

def desconto_inss(salario_bruto):
    inss = salario_bruto * 0.10
    return inss

def calculo_fgts(salario_bruto):
    fgts = salario_bruto * 0.11
    return fgts

def aliquota_ir(salario_bruto):
    if (salario_bruto <= 900):
        aliquota = "Isento"
        return aliquota
    
    elif (salario_bruto >= 901 and salario_bruto <= 1500):
        aliquota = "5%"
        return aliquota
    
    elif (salario_bruto >= 1501 and salario_bruto <= 2500):
        aliquota = "10%"
        return aliquota
    
    elif (salario_bruto >= 2501):
        aliquota = "20%"
        return aliquota
    
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
valor_hora_trabalhada = float(input('Digite o valor da hora trabalhada: '))

salario_bruto_total = calculo_salario_bruto(horas_trabalhadas, valor_hora_trabalhada)

desconto_do_ir = desconto_ir(salario_bruto_total)
desconto_do_sindicato = desconto_sindicato(salario_bruto_total)
desconto_do_inss = desconto_inss(salario_bruto_total)
fgts = calculo_fgts(salario_bruto_total)
aliquota_do_ir = aliquota_ir(salario_bruto_total)

total_descontos = desconto_do_ir + desconto_do_sindicato + desconto_do_inss
salario_liquido = salario_bruto_total - total_descontos

main = (f"""
-     Salário Bruto: ({valor_hora_trabalhada:.2f} * {horas_trabalhadas:.0f})       : R$ {salario_bruto_total:.2f}
-       (-) IR ({aliquota_do_ir})                     : R$ {desconto_do_ir:.2f}  
-       (-) INSS (10%)                  : R$ {desconto_do_inss:.2f}
-       (-) Sindicato                   : R$ {desconto_do_sindicato:.2f} 
-           FGTS (11%)                  : R$ {fgts:.2f}
-           Total de descontos          : R$ {total_descontos:.2f}
-           Salário Liquido             : R$ {salario_liquido:.2f} 
"""
        )

print(main)