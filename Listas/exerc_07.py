#7.	Faça um Programa que leia um vetor de 5 números inteiros, 
# mostre a soma, a multiplicação e os números.

print('5 NUMEROS INTEIROS'.center(60))
print('-' * 60)
print('')

numeros = []

for i in range(5):
    x = int(input('Digite um numero inteiro: '))
    numeros.append(x)

def multiplicacao(numeros):
    resultado = 1
    for i in numeros:
        resultado *= i
    return resultado


soma = sum(numeros)
resultadoMulti = multiplicacao(numeros)


print(f' A soma nos numeros digitados é: {soma} \n Os numero multiplicados tem o resultado: {resultadoMulti} \n Os numeros digitados foram: {numeros}. ')