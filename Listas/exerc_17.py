'''
17.	Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. 

Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 

O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

| Atleta            | Primeiro Salto | Segundo Salto | Terceiro Salto | Quarto Salto | Quinto Salto |
|-------------------|----------------|---------------|----------------|--------------|--------------|
| Rodrigo Curvêllo  | 6.5 m          | 6.1 m         | 6.2 m          | 5.4 m        | 5.3 m        |

| Resultado Final   |
|-------------------|
| Média: 5.9 m      |

'''


print('MEDIA DE SALTOS'.center(60))
print('-' * 60)


saltos = []
atleta = input('\n Por favor digite o nome do atleta que vai saltar: ')

for i in range(5):
    salto = float(input(f'Digite a nota do salto {i+1}: '))
    saltos.append(salto)


media = sum(saltos) / 5

print(f'''
| Atleta            | Primeiro Salto | Segundo Salto | Terceiro Salto | Quarto Salto | Quinto Salto |
|-------------------|----------------|---------------|----------------|--------------|--------------|
| {atleta}           |{saltos [0]}m           |{saltos [1]}m          |{saltos [2]}m           |{saltos [3]}m         |{saltos [4]}m         |

| Resultado Final   |
|-------------------|
|Média: {media} m      |


''')