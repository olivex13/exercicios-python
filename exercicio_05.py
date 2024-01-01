# 5.	Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#-	A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#-	A mensagem "Reprovado", se a média for menor do que sete;
#-	A mensagem "Aprovado com Distinção", se a média for igual a dez.

print('Calculadora de média'.center (60))
print('')

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2


if (media == 10):
    print(f'Sua média foi {media} e você foi aprovado com destinção.')
elif (media >= 7):
    print(f'Sua média é {media} e você foi aprovado.')
elif (media < 7):
    print(f'Sua média foi {media} e você está reprovado.')
