def eh_perfeito(x: int) -> bool:
    todos_divisores: list[int] = []

    for i in range(1, x):
        if x % i == 0:
            todos_divisores.append(i)

    return sum(todos_divisores) == x


n: int = int(input())

for _ in range(n):
    x: int = int(input())

    if eh_perfeito(x):
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
