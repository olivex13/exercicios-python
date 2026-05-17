# exercicio 20

print("=" * 46)
print("Projeção de Gastos com Abono".center(46))
print("=" * 46)

salarios = []
abonos = []

while True:
    salario = float(input("Digite o salário: "))
    if salario == 0:
        break
    salarios.append(salario)
    abono = salario * 0.20
    if abono < 100:
        abono = 100
    abonos.append(abono)

print("=" * 46)
print(f"{'Salário':<22} {'Abono':>6}")
print("-" * 46)

for i, salario in enumerate(salarios):
    print(f"R$ {salario:<22.2f} R$ {abonos[i]:<6.2f}")

print("-" * 46)
print(f"Total de colaboradores: {len(salarios)}")
print(f"Total gasto com abonos: R$ {sum(abonos):.2f}")
print(f"Valor mínimo pago a {abonos.count(100)} colaboradores")
print(f"Maior valor de abono pago: R$ {max(abonos):.2f}")
print("=" * 46)