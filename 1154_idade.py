idades: list[int] = []
contador = 0

while True:
    idade = int(input())

    if idade < 0:
        break

    idades.append(idade)
    contador += 1

print(f"{sum(idades) / contador:.2f}")
