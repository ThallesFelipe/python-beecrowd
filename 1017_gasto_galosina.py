tempo_viagem_horas = int(input())
velocidade_media = int(input())

KM_POR_LITRO = 12

combustivel_gasto = (tempo_viagem_horas * velocidade_media) / KM_POR_LITRO

print(f"{combustivel_gasto:.3f}")
