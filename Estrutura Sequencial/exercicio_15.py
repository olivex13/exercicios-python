#Faça um programa que peça o tamanho de um arquivo para download (em MB) 
#e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print('==========Tempo de Download=========')

tamanho_arquivo = float(input('Digite o tamanho no arquivo(mb): '))
velocidade_internet = float(input('Digite a velocidade do link e internet(mbps): '))
arquivo_bits = tamanho_arquivo * 8

tempo_download = arquivo_bits / velocidade_internet
print('')

print(f'O arquivo de tamanho {tamanho_arquivo:.0f} mb, vai levar {tempo_download:.0f} minutos para baixar')
print('')