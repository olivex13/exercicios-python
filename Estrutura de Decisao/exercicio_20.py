'''Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:
- a.	A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
- b.	A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
- c.	A mensagem "Aprovado com Distinção", se a média for igual a 10. '''

print("<==========CALCULADORA DE NOTAS ESCOLA DO PYTHON==========>".center(120))
print('')

def calculadora_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

def status_final(media):
    if (media == 10):
        status = "Aprovado com Distinção"
    elif (media < 7):
        status = "Reprovado"
    else: 
        status = "Aprovado"
    
    return status

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))

media_final = calculadora_media(nota_1, nota_2, nota_3)
resultado = status_final(media_final)

print(f'O resultado das duas notas é: {resultado}')