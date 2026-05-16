#EXERCICIO 48

print("=" * 46)
print('INVERTENDO NUMEROS INTEIROS'.center(46))
print("=" * 46)

while True:
    try:
        numero = int(input("Digite um numero inteiro: "))
        if numero > 0:
            break
        else:
            print("O numero deve ser inteiro positivo.")
    except ValueError:
        print("Valor invalido. Digite um numero inteiro.")

numero_invertido = int(str(numero)[::-1])
print(f"O numero {numero} invertido eh {numero_invertido}")