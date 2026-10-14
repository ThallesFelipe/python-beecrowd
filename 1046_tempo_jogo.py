inicio, fim = map(int, input().split())

if inicio == fim:
    print("O JOGO DUROU 24 HORA(S)")
elif inicio > fim:
    tempo_total = (24 - inicio) + fim
    print(f"O JOGO DUROU {tempo_total} HORA(S)")
else:
    tempo_total = fim - inicio
    print(f"O JOGO DUROU {tempo_total} HORA(S)")
