#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#a.	par ou ímpar;
#b.	positivo ou negativo; 
#c.	inteiro ou decimal.

print('==========ANALISANDO NUMEROS=========='.center(120))
print('')

def multiplicacao(nmr_1, nmr_2):
    return nmr_1 * nmr_2

def soma(nmr_1, nmr_2):
    return nmr_1 + nmr_2

def divisao(nmr_1, nmr_2):
    return nmr_1 / nmr_2

def subtracao(nmr_1, nmr_2):
    return nmr_1 - nmr_2

nmr_1 = float(input('Digite o primeiro numero: '))
print('')
nmr_2 = float(input('Digite o segundo numero: '))
print('')

operacao = str(input(""" Qual operação deseja fazer ?
                        [A] Multiplicação
                        [B] Soma
                        [C] Divisão
                        [D] Subtração                            
                        """)).lower()


if (operacao == 'a'):
    total = multiplicacao(nmr_1, nmr_2)
    if (total % 2 == 0):
        letra_a = "O numero é par"
    else:
        letra_a = "O numero é impar"
    
    if (total >= 0):
        letra_b = 'O numero é positivo'
    else:
        letra_b = 'O numero é negativo'
    if isinstance(total, int):
        letra_c = 'O numero é inteiro'
    else: 
        letra_c = 'O numero é decimal'

elif (operacao == 'b'):
    total = soma(nmr_1, nmr_2)
    if (total % 2 == 0):
        letra_a = "O numero é par"
    else:
        letra_a = "O numero é impar"
    
    if (total >= 0):
        letra_b = 'O numero é positivo'
    else:
        letra_b = 'O numero é negativo'
    if isinstance(total, int):
        letra_c = 'O numero é inteiro'
    else: 
        letra_c = 'O numero é decimal'

elif (operacao == 'c'):
    total = divisao(nmr_1, nmr_2)
    if (total % 2 == 0):
        letra_a = "O numero é par"
    else:
        letra_a = "O numero é impar"
    
    if (total >= 0):
        letra_b = 'O numero é positivo'
    else:
        letra_b = 'O numero é negativo'
    if isinstance(total, int):
        letra_c = 'O numero é inteiro'
    else: 
        letra_c = 'O numero é decimal'
elif (operacao == 'd'):
    total = subtracao(nmr_1, nmr_2)
    if (total % 2 == 0):
        letra_a = "O numero é par"
    else:
        letra_a = "O numero é impar"
    
    if (total >= 0):
        letra_b = 'O numero é positivo'
    else:
        letra_b = 'O numero é negativo'
    if isinstance(total, int):
        letra_c = 'O numero é inteiro'
    else: 
        letra_c = 'O numero é decimal'

else:
    print('Digite uma opção válida.')

print('')
print(f"""O resultado dos numeros digitados é {total}
           [A] {letra_a}
           [B] {letra_b}
           [C] {letra_c}
""")