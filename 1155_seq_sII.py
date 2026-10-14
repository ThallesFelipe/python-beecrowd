s: float = 0

denominador = 1

for i in range(1, 40, 2):
    s += i / denominador
    denominador *= 2

print(f"{s:.2f}")
