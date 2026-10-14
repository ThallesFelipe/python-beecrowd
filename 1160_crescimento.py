t: int = int(input())

for _ in range(t):
    popu_a, popu_b, cresc_a, cresc_b = input().split()
    popu_a, popu_b, cresc_a, cresc_b = (
        int(popu_a),
        int(popu_b),
        float(cresc_a),
        float(cresc_b),
    )

    if popu_a > popu_b:
        popu_a, popu_b = popu_b, popu_a

    tempo_em_anos = 0

    while popu_a <= popu_b and tempo_em_anos <= 100:
        qtd_nascidos_a = int(popu_a * (cresc_a / 100))
        qtd_nascidos_b = int(popu_b * (cresc_b / 100))

        popu_a += qtd_nascidos_a
        popu_b += qtd_nascidos_b
        tempo_em_anos += 1

    if tempo_em_anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{tempo_em_anos} anos.")
