# 10.	Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, 
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

print('VETORES INTERCALADOS'.center(60))
print('-' * 60)
print('')

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    numero = int(input(" Digite um numero para o vetor: "))
    vetor1.append(numero)

for i in range(10):
    numero2 = int(input("Digite um numero para o outro vetor: "))
    vetor2.append(numero2)

for i in range(10): 
    vetor3.append(vetor1[i]) 
    vetor3.append(vetor2[i])  


print(f"Vetor intercalado: {vetor3}")