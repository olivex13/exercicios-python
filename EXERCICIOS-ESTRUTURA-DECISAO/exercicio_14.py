'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
-	  Média de Aproveitamento  Conceito
-	  Entre 9.0 e 10.0        A
-	  Entre 7.5 e 9.0         B
-	  Entre 6.0 e 7.5         C
-	  Entre 4.0 e 6.0         D
-	  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C 
ou “REPROVADO” se o conceito for D ou E.'''

print("=====RESULTADO ACADEMICO=====".center(60))
print('')

def media_aluno (n1, n2):
    media = (n1 + n2) / 2
    return media    

def conceito (media):
    if (media >= 0 and media <= 3.9):
        return "E"
    elif (media >= 4 and media <= 5.9):
        return "D"
    elif (media >= 6 and media <= 7.4):
        return "C"
    elif (media >= 7.5 and media <= 8.9):
        return "B"
    elif (media >= 9 and media <= 10):
        return "A"

def status_academico(conceito_aluno):
    if (conceito_aluno == "A"):
        return "Aprovado"
    elif (conceito_aluno == "B"):
        return "Aprovado"
    elif (conceito_aluno == "C"):
        return "Aprovado"
    elif (conceito_aluno == "D"):
        return "Reprovado"
    elif (conceito_aluno == "F"):
        return "Reprovado"
    
nota_1 = float(input('Digite a primeira nota do aluno: '))
print('')
nota_2 = float(input('Digite a segunda nota: '))
print("")

media = media_aluno(nota_1, nota_2)
conceito_aluno = conceito(media)    
status = status_academico(conceito_aluno)
    
tela = (f"""
Segue as notas que foram tiradas pelo aluno:
Nota 1 = {nota_1:.0f}
Nota 2 = {nota_2:.0f}
Media = {media}
Conceito = {conceito_aluno}
Status: {status}
""")

print(tela)