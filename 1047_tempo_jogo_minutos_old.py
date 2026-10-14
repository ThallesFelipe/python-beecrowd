inicio_hora, inicio_minuto, fim_hora, fim_minuto = map(int, input().split())

HORAS_DIA = 24
MINUTOS_HORA = 60

if inicio_hora == fim_hora and inicio_minuto == fim_minuto:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

elif inicio_hora > fim_hora or (inicio_hora == fim_hora and inicio_minuto > fim_minuto):
    horas_totais = (HORAS_DIA - inicio_hora) + fim_hora

    if inicio_minuto > fim_minuto:
        horas_totais -= 1
        minutos_totais = (MINUTOS_HORA - inicio_minuto) + fim_minuto
    else:
        minutos_totais = fim_minuto - inicio_minuto

    print(f"O JOGO DUROU {horas_totais} HORA(S) E {minutos_totais} MINUTO(S)")

else:
    horas_totais = fim_hora - inicio_hora

    if inicio_minuto > fim_minuto:
        horas_totais -= 1
        minutos_totais = (MINUTOS_HORA - inicio_minuto) + fim_minuto
    else:
        minutos_totais = fim_minuto - inicio_minuto

    print(f"O JOGO DUROU {horas_totais} HORA(S) E {minutos_totais} MINUTO(S)")
