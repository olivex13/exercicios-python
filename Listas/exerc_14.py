"""14.	Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:
-          a.	"Telefonou para a vítima?"
           b.	"Esteve no local do crime?"
           c.	"Mora perto da vítima?"
           d.	"Devia para a vítima?"
           e.	"Já trabalhou com a vítima?" 
           
           O programa deve no final emitir uma classificação sobre a 
           participação da pessoa no crime. Se a pessoa responder positivamente a 
           2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 
           como "Assassino". Caso contrário, ele será classificado como "Inocente".
           
           """

print('Investigação Criminal'.center(60))
print('-' * 60)
print('')

respostasPositivas = []

print('Responda as perguntas a seguir com SIM ou NÃO: \n')

while True:
    perguntaA = input('Telefonou para a vítima?: ')
    if perguntaA.lower() == "sim":
        respostasPositivas.append("Telefonou para a vítima")
        break
    elif perguntaA.lower() == "nao" or perguntaA.lower() == "não":
        break
    else:
        print("Responda com 'Sim' ou 'Não' ")

while True:
    perguntaB = input('Esteve no local do crime?: ')
    if perguntaB.lower() == "sim":
        respostasPositivas.append("Esteve no local do crime")
        break
    elif perguntaB.lower() == "nao" or perguntaB.lower() == "não":
        break
    else:
        print("Responda com 'Sim' ou 'Não' ")

while True:
    perguntaC = input('Mora perto da vítima?: ')
    if perguntaC.lower() == "sim":
        respostasPositivas.append("Mora perto da vítima")
        break
    elif perguntaC.lower() == "nao" or perguntaC.lower() == "não":
        break
    else:
        print("Responda com 'Sim' ou 'Não' ")

while True:
    perguntaD = input('Devia para a vítima?: ')
    if perguntaD.lower() == "sim":
        respostasPositivas.append("Devia para a vítima")
        break
    elif perguntaD.lower() == "nao" or perguntaD.lower() == "não":
        break
    else:
        print("Responda com 'Sim' ou 'Não' ")

while True:
    perguntaE = input("Já trabalhou com a vítima?: ")
    if perguntaE.lower() == "sim":
        respostasPositivas.append("Esteve no local do crime")
        break
    elif perguntaE.lower() == "nao" or perguntaE.lower() == "não":
        break
    else:
        print("Responda com 'Sim' ou 'Não' ")


contador = 0
for i in respostasPositivas:
    contador += 1

if contador == 2:
    veredito = 'Suspeito'
elif contador == 3 or contador == 4:
    veredito = 'Cúmplice'
elif contador == 5:
    veredito = 'Assasino'
else:
    veredito = 'Inocente'


print('')
print(f'O resultado da investigação foi: \n {respostasPositivas} \n O individuo é: {veredito}')