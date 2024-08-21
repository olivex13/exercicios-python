#12. Foram anotadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior 
# à média de altura desses alunos.

print('MEDIA DE ALTURA DE ALUNOS'.center(60))
print('-' * 60)
print('')

alturas = []
idades = []

for i in range(30):
    altura = float(input(f'Digite a altura do aluno {i+1}: '))
    idade = int(input(f'Digite a idade do aluno {i+1}: '))
    alturas.append(altura)
    idades.append(idade)   

mediaAltura = sum(alturas) / 30

print(f'A media de altura dos alunos é {mediaAltura}.')

contadorAluno = 0

for altura, idade in zip(alturas, idades):
    if idade >= 13 and altura < mediaAltura:
        contadorAluno += 1

print(f'A quantidade de alunos com mais de 13 anos com altura inferior a média de altura é {contadorAluno}.'
      ) 