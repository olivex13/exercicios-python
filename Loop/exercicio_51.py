#exercicio 51
print("=" * 46)
print('CALCULANDO VALOR DE S'.center(46))
print("=" * 46)

while True:
    try:
        termos = int(input("Digite a quantidade de termos: "))
        if termos > 0:
            break
        else:
            print("O numero deve ser inteiro positivo.")
    except ValueError:
        print("Valor invalido. Digite um numero inteiro.")


numerador = []
denominador = []
soma_total = 0

for i in range(1, termos + 1):
    numerador.append(i)
    denominador.append(i * 2 - 1)

for i in range(len(numerador)):
    
    num = numerador[i]
    den = denominador[i]
    
    soma_total += num / den

    print(f"Termo {i+1}: {num}/{den}")

print("---")
print(f"A soma final da série é: {soma_total:.2f}")