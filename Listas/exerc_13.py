# 13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#  e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

print('MEDIA DE TEMPERATURA'.center(60))
print('-' * 60)
print('')

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mediaTemperatura = []

for mes in meses:
    temperatura = float(input(f'Digite a média de temperatura de {mes}: '))
    mediaTemperatura.append(temperatura)

mediaAnual = sum(mediaTemperatura) / 12

print('')
print(f'A média de temperatura anual foi {mediaAnual:.2f}')
print('')
for mes, temperatura in zip(meses, mediaTemperatura):
    if temperatura > mediaAnual:
        print(f'A temperatura em {mes} foi maior que a média anual atingindo {temperatura} graus.')