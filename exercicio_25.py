'''25.	Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a.	"Telefonou para a vítima?"
b.	"Esteve no local do crime?"
c.	"Mora perto da vítima?"
d.	"Devia para a vítima?"
e.	"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".'''

print('<=====INVESTIGAÇÃO CRIMINAL======>'.center(60))
print('')

main = """Atenção, você esta sendo investigado.
Responda as perguntas a seguir com:
            SIM ou NÃO"""

print(main)
print("")

pergunta1 = str(input('Voce telefonou para a vitima? => ')).lower()
pergunta2 = str(input('Esteve no local do crime? => ')).lower()
pergunta3 = str(input('Mora perto da Vitima? => ')).lower()
pergunta4 = str(input('Devia para a vitima? => ')).lower()
pergunta5 = str(input('Ja trabalhou com a vítima? => ')).lower()
contagem = None

def status(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5):

    resultado = 0

    if (pergunta1 == 'sim'):
        resultado += 1
    else:
        resultado += 0
    
    if (pergunta2 == 'sim'):
        resultado += 1
    else:
        resultado += 0
    
    if (pergunta3 == 'sim'):
        resultado += 1
    else:
        resultado += 0

    if (pergunta4 == 'sim'):
        resultado += 1
    else:
        resultado += 0
    
    if (pergunta5 == 'sim'):
        resultado += 1
    else:
        resultado += 0

    return resultado

def apuracao(resultado):
    if (resultado == 2):
        return "Você é suspeito!"
    elif (resultado >= 3 and resultado <=4):
        return "Você é cúmplice!"
    elif (resultado == 5):
        return "Você é o assasino!"
    else:
        return "Você é inocente!"
    
contagem = status(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5)

veredito = apuracao(contagem)


print(f'De acordo com o resultado da investigação, {veredito}')