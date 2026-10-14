dia_inicio = int(input().split()[1])
h_inicio, m_inicio, s_inicio = map(int, input().split(" : "))

dia_fim = int(input().split()[1])
h_fim, m_fim, s_fim = map(int, input().split(" : "))

total_inicio = dia_inicio * 24 * 3600 + h_inicio * 3600 + m_inicio * 60 + s_inicio
total_fim = dia_fim * 24 * 3600 + h_fim * 3600 + m_fim * 60 + s_fim

total_segundos = total_fim - total_inicio

dias = total_segundos // (24 * 3600)
total_segundos %= 24 * 3600
horas = total_segundos // 3600
total_segundos %= 3600
minutos = total_segundos // 60
total_segundos %= 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{total_segundos} segundo(s)")
