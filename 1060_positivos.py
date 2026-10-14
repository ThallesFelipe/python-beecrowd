contador: int = 0
for i in range(6):
    n: float = float(input())
    if n >= 0:
        contador += 1

print(f"{contador} valores positivos")
