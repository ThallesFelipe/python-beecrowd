contador: int = 0

positivos: list[float] = []

for i in range(6):
    n: float = float(input())
    if n >= 0:
        positivos.append(n)
        contador += 1

print(f"{contador} valores positivos")
print(round((sum(positivos) / contador), 1))
