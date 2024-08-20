# 11.	Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
print('VETORES INTERCALADOS'.center(60))
print('-' * 60)
print('')

vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

print('Adcione 10 numeros para cada vetor')

for i in range(10):
    numero = int(input(f" Digite o numero {i+1} para o primeiro vetor: "))
    vetor1.append(numero)

for i in range(10):
    numero2 = int(input(f" Digite o numero {i+1} para o segundo vetor: "))
    vetor2.append(numero2)

for i in range(10):
    numero3 = int(input(f" Digite o numero {i+1} para o terceiro vetor: "))
    vetor3.append(numero3)

for i in range(10): 
    vetor4.append(vetor1[i]) 
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])  


print(f"Vetor intercalado: {vetor4}")