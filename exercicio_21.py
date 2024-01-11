'''21.	Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

print('==========CAIXA ELETRONICO DO PYTHON=========='.center(120))
print('')

def calcular_notas(valor):
    notas_disponiveis = [100, 50, 10, 5, 1]
    quantidade_notas = [0, 0, 0, 0, 0]

    for i in range(len(notas_disponiveis)):
        while valor >= notas_disponiveis[i]:
            valor -= notas_disponiveis[i]
            quantidade_notas[i] += 1

    return quantidade_notas

def main():
    valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))
    
    if valor_saque < 10 or valor_saque > 600:
        print("Valor de saque inválido. O valor deve estar entre 10 e 600 reais.")
        return

    notas = calcular_notas(valor_saque)
    notas_disponiveis = [100, 50, 10, 5, 1]
    print(f"Notas fornecidas para sacar {valor_saque} reais:")
    for i in range(len(notas)):
        if notas[i] > 0:
            print(f"{notas[i]} nota(s) de {notas_disponiveis[i]} reais")

if __name__ == "__main__":
    main()
def saque(valor):
    if valor >= 10 and valor <=600:
        return f'Você está sacando R$ {valor:.2f}.'
    else:
        return ''