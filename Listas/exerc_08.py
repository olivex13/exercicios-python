# 8.	Faça um Programa que peça a idade e a altura de 5 pessoas, 
# armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

print('IMPRIMINDO A IDADE DAS PESSOAS'.center(60))
print('-' * 60)
print('')

vetorIdade = []
vetorAltura = []

for i in range(5):
    altura = float(input(f'Digite a altura da pessoa {i+1}: '))
    print('')
    vetorAltura.append(altura)
    idade = int(input(f'Digite a idade da pessoa {i + 1}:  '))
    vetorIdade.append(idade)
    print('')

for i in range(4, -1, -1):
    print(f' A idade da pessoa {i + 1} é: {vetorIdade[i]}.')
    print(f'A altura da pessoa {i+1} é: {vetorAltura[i]}.')


