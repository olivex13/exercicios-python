''' Faça um Programa que leia um número inteiro menor que 1000 
 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
 Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades 

 Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 '''

print('==========NUMERO POR EXTENSO=========='.center(120))
print('')

def imprimir_numero_extenso(numero):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    resultado = ""

    if centenas > 0:
        resultado += f"{centenas} centena(s)"
        if dezenas > 0 or unidades > 0:
            resultado += ", "

    if dezenas > 0:
        resultado += f"{dezenas} dezena(s)"
        if unidades > 0:
            resultado += " e "

    if unidades > 0:
        resultado += f"{unidades} unidade(s)"

    print(resultado)


numeros_teste = [326, 12, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

for numero in numeros_teste:
    print(f"{numero} = ", end="")
    imprimir_numero_extenso(numero)