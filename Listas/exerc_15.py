#15.	Faça um programa que leia um número indeterminado de valores, 
# correspondentes a notas, encerrando a entrada de dados quando for informado um valor 
# igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

''''- a.	Mostre a quantidade de valores que foram lidos;
- b.	Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
- c.	Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
- d.	Calcule e mostre a soma dos valores;
- e.	Calcule e mostre a média dos valores;
- f.	Calcule e mostre a quantidade de valores acima da média calculada;
- g.	Calcule e mostre a quantidade de valores abaixo de sete;
- h.	Encerre o programa com uma mensagem;'''

print('LENDO VALORES'.center(60))
print('-' * 60)
print('')


valores = []

print("Digite a quantidade de valores necessários, quando desejar encerrar, digite '-1'")

while True:
    valor = float(input('Digite um valor: '))
    if valor == -1:
        break
    else:
        valores.append(valor)

valoresDigitados = 0

for i in valores:
    valoresDigitados += 1

print('')
print(f'Foram lidos {valoresDigitados} valores. \n')
print(f'Os valores digitados foram: {valores} \n')
print('Valores impressos em ordem inversa, um em baixo do outro. \n')

for i in reversed(valores):
    print(i)

print('')
somaValores = sum(valores)

mediaValores = somaValores / valoresDigitados

print(f'A soma dos valores digitados é: {somaValores} \n')
print(f' A média dos valores digitados é: {mediaValores} \n')

acimaDaMedia = []
valoresAbaixo = []

for valor in valores:
    if valor > mediaValores:
        acimaDaMedia.append(valor)
    elif valor < 7:
        valoresAbaixo.append(valor)

print(f'Os valores acima da média digitados foram: \n {acimaDaMedia} \n')
print(f'Os valores abaixo de 7 digitados foram: \n {valoresAbaixo} \n')
print('Programa encerrado com sucesso.')





