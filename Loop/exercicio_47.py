# EXERCICIO 47

def atletas():
  qntAtletas = int(input("Digite a quantidade de atletas: "))
  print("")
  atletas = []
  for i in range(qntAtletas):
    atletas.append(input(f"Digite o nome do(a) atleta {i+1}: "))
  return atletas

def jurados():
    jurados = []
    for i in range(7):
        jurados.append(input(f'Digite o nome do jurado {i+1}: '))
    return jurados

def notas(atletas, jurados):
    resultado_notas = {}
    for nome in atletas:
        print(f'Notas do(a) Atleta {nome}'.center(46))
        notas_deste_atleta = []
        for nome_jurado in jurados:
            while True:
                nota = float(input(f'Nota do Jurado {nome_jurado}: '))
                if nota < 0 or nota > 10:
                    print("Nota inválida! Digite uma nota entre 0 e 10.")
                else: 
                    notas_deste_atleta.append(nota)
                    break
        resultado_notas[nome] = notas_deste_atleta
    return resultado_notas        
        
def resultado(notas, jurados):
    for nome, lista_notas in notas.items():
        print("=" * 44 + "\n")
        print(f'| {"Atleta":<20} | {nome:<20} |')
        print(f'|{"-"*22}|{"-"*22}|')
        for jurado, nota in zip(jurados, lista_notas):
            print(f'| {jurado:<20} | {nota:<20} |')
        pior_nota = min(lista_notas)
        melhor_nota = max(lista_notas)
        notas_filtradas = lista_notas.copy()
        notas_filtradas.remove(pior_nota)
        notas_filtradas.remove(melhor_nota)
        media = sum(notas_filtradas) / len(notas_filtradas)
        print(f'| {"Resultado Final":<20} | {"":20} |')
        print(f'| {"Melhor Nota":<20} | {melhor_nota:<20} |')
        print(f'| {"Pior Nota":<20} | {pior_nota:<20} |')
        print(f'| {"Média":<20} | {media:<20.2f} |')

print("=" * 46)
print('NOTAS DOS ATLETAS'.center(46))
print("=" * 46)
lista_atletas = atletas()
print("=" * 46)
print('SELEÇÃO DE JURADOS'.center(46))
lista_jurados = jurados()
print("=" * 46)
dicionario = notas(lista_atletas, lista_jurados)
resultado(dicionario, lista_jurados)


