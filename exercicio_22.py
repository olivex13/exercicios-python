#22.	Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

print("<==========PAR OU IMPAR?==========>".center(120))
print("")

def par_impar(numero):
    if (numero % 2 == 0):
        resultado = "O numero digitado é par"
    else:
        resultado = "O numero digitado é impar"
       
    return resultado
    
numero_digitado = int(input('Digite o numero desejado: '))

par_ou_impar = par_impar(numero_digitado)

print(par_ou_impar)