
#exercicio 46

NOMES_SALTOS = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']


def coletar_saltos(nome):
    print(f'Saltos do(a) Atleta {nome}'.center(46))
    saltos = []
    for ordem in NOMES_SALTOS:
        while True:
            try:
                distancia = float(input(f'  {ordem} salto (m): '))
                saltos.append(distancia)
                break
            except ValueError:
                print('  Valor inválido. Digite um número.')
    return saltos


def exibir_resultado(nome, saltos):
    melhor = max(saltos)
    pior = min(saltos)

    saltos_restantes = saltos.copy()
    saltos_restantes.remove(melhor)
    saltos_restantes.remove(pior)
    media = sum(saltos_restantes) / len(saltos_restantes)

    print('=' * 46 + '\n')
    print(f'| {"Atleta":<20} | {nome:<20} |')
    print(f'|{"-" * 22}|{"-" * 22}|')
    for ordem, dist in zip(NOMES_SALTOS, saltos):
        rotulo = f'{ordem} Salto'
        valor  = f'{dist:.1f} m'
        print(f'| {rotulo:<20} | {valor:<20} |')
    print(f'|{"-" * 22}|{"-" * 22}|')
    print(f'| {"Melhor Salto":<20} | {f"{melhor:.1f} m":<20} |')
    print(f'| {"Pior Salto":<20} | {f"{pior:.1f} m":<20} |')
    print(f'| {"Média dos demais":<20} | {f"{media:.1f} m":<20} |')
    print(f'| {"Resultado Final":<20} | {f"{media:.1f} m":<20} |')

print('=' * 46)
print('COMPETIÇÃO DE SALTO EM DISTÂNCIA'.center(46))
print('=' * 46)

while True:
    print()
    nome = input('Nome do atleta (ou ENTER para encerrar): ').strip()

    if nome == '':
        break

    print('=' * 46)
    saltos = coletar_saltos(nome)
    exibir_resultado(nome, saltos)

print()
print('=' * 46)
print('Programa encerrado.'.center(46))
print('=' * 46)
