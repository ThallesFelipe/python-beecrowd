inicio_hora, inicio_minuto, fim_hora, fim_minuto = map(int, input().split())

MINUTOS_POR_HORA = 60
MINUTOS_POR_DIA = 24 * MINUTOS_POR_HORA

inicio = inicio_hora * MINUTOS_POR_HORA + inicio_minuto
fim = fim_hora * MINUTOS_POR_HORA + fim_minuto

duracao = fim - inicio

if duracao <= 0:
    duracao += MINUTOS_POR_DIA

horas = duracao // MINUTOS_POR_HORA
minutos = duracao % MINUTOS_POR_HORA

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
