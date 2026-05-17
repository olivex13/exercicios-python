#exercicio 21

print("=" * 46)
print("Autonomia de Veículos".center(46))
print("=" * 46)

veiculos = []
consumos = []
gasolina = 2.25

while True:
    veiculo = input("Digite o nome do veículo: ")
    veiculos.append(veiculo)
    consumo = float(input("Digite o consumo do veículo (km/l): "))
    consumos.append(consumo)
    if len(veiculos) == 5:
        break

print("\n" + "=" * 46)
print(f"{'Veículo':<18} | {'Nome':>8} | {'Km por litro':>12}")
print("-" * 46)

for i, veiculo in enumerate(veiculos):
    print(f"{'Veículo ' + str(i + 1):<18} | {veiculo:>8} | {consumos[i]:>12.1f}")

consumo_litros = []
custos = []

for i in range(len(veiculos)):
    consumo_litros.append(1000 / consumos[i])
    custos.append(consumo_litros[i] * 2.25)

print("\n" + "=" * 62)
print(f"{'Nº':<3} | {'Veículo':>10} | {'Km por litro':>12} | {'Consumo (litros)':>16} | {'Custo (R$)':>10}")
print("-" * 62)
for i, veiculo in enumerate(veiculos):
    print(f"{i + 1:<3} | {veiculo:>10} | {consumos[i]:>12.1f} | {consumo_litros[i]:>16.2f} | R$ {custos[i]:>7.2f}")

menor_custo = min(custos)
veiculo_economico = veiculos[custos.index(menor_custo)]
print(f"\nO veículo mais econômico é o {veiculo_economico} com custo de R$ {menor_custo:.2f} para 1000 km.")
