#EXERCÍCIO 22

print("=" * 46)
print("Manutenção de Mouses".center(46))
print("=" * 46)

esfera = 0
limpeza = 0
cabo = 0
quebrado = 0
total = 0
defeitos = ["Necessita da esfera", "Necessita de limpeza", "Necessita troca do cabo ou conector", "Quebrado ou inutilizado"]

print("\nDefeitos:".center(46))
print("-" * 46)
for i in range(len(defeitos)):
    print(f"{i + 1} - {defeitos[i]}")

while True:
    mouse = int(input("Digite o número de identificação do mouse: "))
    if mouse == 0:
        break
    tipo = int(input("Digite o tipo de defeito: "))
    if tipo == 1:
        esfera += 1
    elif tipo == 2:
        limpeza += 1
    elif tipo == 3:
        cabo += 1
    elif tipo == 4:
        quebrado += 1
    total += 1

print("\n" + "=" * 46)
print("Relatório de Defeitos".center(46))
print("=" * 46)

if total == 0:
    print("Nenhum mouse foi cadastrado.")
else:
    print(f"{'Situação':<40} | {'Quantidade':<10} | {'Percentual':<10}")
    print("-" * 66)
    print(f"{'1 - Necessita da esfera':<40} | {esfera:<10} | {(esfera / total * 100):<10.2f}%")
    print(f"{'2 - Necessita de limpeza':<40} | {limpeza:<10} | {(limpeza / total * 100):<10.2f}%")
    print(f"{'3 - Necessita troca do cabo ou conector':<40} | {cabo:<10} | {(cabo / total * 100):<10.2f}%")
    print(f"{'4 - Quebrado ou inutilizado':<40} | {quebrado:<10} | {(quebrado / total * 100):<10.2f}%")
    print("-" * 66)
    print(f"{'Total':<40} | {total:<10} | {100.00:<10.2f}%")