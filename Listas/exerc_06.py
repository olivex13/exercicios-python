#6.	Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno,
#  imprima o número de alunos com média maior ou igual a 7.0.

print('MEDIAS APROVADAS'.center(60))
print('-' * 60)
print('')

medias = []
mediasAprovadas = []

for i in range(10):
    print(f'Digite as notas do aluno {i+1} \n ')
    notas = []
    nota1 = float(input('Digite a primeira nota: '))
    notas.append(nota1)
    nota2 = float(input('Digite a segunda nota: '))
    notas.append(nota2)
    nota3 = float(input('Digite a terceira nota: '))
    notas.append(nota3)
    nota4 = float(input('Digite a quarta nota: '))
    print('')
    notas.append(nota4)
    mediaAluno = sum(notas) / 4
    medias.append(mediaAluno)

for i in medias:
    if i >= 7:
        mediasAprovadas.append(i)

print(f'As medias aprovadas foram: {mediasAprovadas}')