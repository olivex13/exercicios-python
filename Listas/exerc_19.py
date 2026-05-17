# exercicio 19

sistemas_operacionais = [
    "Windows Server",
    "Unix",
    "Linux",
    "Netware",
    "Mac OS",
    "Outro"
]

def coletar_votos(sistemas_operacionais):
    """Exibe os candidatos com suas posições e coleta os votos até o usuário digitar 0."""
    votos = [0] * len(sistemas_operacionais)

    print("=" * 46)
    print("PESQUISA DE SISTEMAS OPERACIONAIS".center(46))
    print("=" * 46)
    print("\nQual o melhor Sistema Operacional para servidores?\n")

    for i, so in enumerate(sistemas_operacionais):
        print(f"  {so} - Digite {i + 1}")
    print("\n  Para encerrar - Digite 0")
    print("-" * 46)

    while True:
        try:
            voto = int(input("\nDigite o voto: "))
        except ValueError:
            print("  Entrada inválida! Digite um número.")
            continue

        if voto == 0:
            print("\nVotação encerrada!")
            break
        elif 1 <= voto <= len(sistemas_operacionais):
            votos[voto - 1] += 1
            print(f"  Voto registrado para: {sistemas_operacionais[voto - 1]}")
        else:
            print(f"  Opcao invalida! Digite um numero entre 1 e {len(sistemas_operacionais)}, ou 0 para encerrar.")

    return votos

votos = coletar_votos(sistemas_operacionais)

total = sum(votos)

print("\n" + "=" * 46)
print(f"{'Sistema Operacional':<22} {'Votos':>6} {'%':>5}")
print("-" * 46)

for i, so in enumerate(sistemas_operacionais):
    percentual = (votos[i] / total * 100) if total > 0 else 0
    print(f"{so:<22} {votos[i]:>6} {percentual:>4.0f}%")

print("-" * 46)
print(f"{'Total':<22} {total:>6}")
print("=" * 46)

if total > 0:
    indice_vencedor = votos.index(max(votos))
    vencedor = sistemas_operacionais[indice_vencedor]
    votos_vencedor = votos[indice_vencedor]
    percentual_vencedor = votos_vencedor / total * 100
    print(f"\nO SO mais votado foi o {vencedor}, com {votos_vencedor} votos ({percentual_vencedor:.0f}%).")
