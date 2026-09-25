def calcular_treino(tempo_total, tempo_volta):
    voltas = tempo_total // tempo_volta
    restante = tempo_total % tempo_volta
    return voltas, restante

def main():
    tempos = [(300, 45), (120, 30), (1000, 50)]
    for tt, tv in tempos:
        v, r = calcular_treino(tt, tv)
        print(f"Tempo Total: {tt}s | Volta: {tv}s")
        print(f"Voltas: {v}")
        print(f"Restante: {r}s")
        print("-" * 20)

if __name__ == "__main__":
    main()