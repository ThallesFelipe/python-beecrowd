n: int = int(input())

for _ in range(n):
    x: int
    y: int
    x, y = map(int, input().split())

    soma_impares: int = 0
    for i in range(x, x + y * 2):
        if i % 2 != 0:
            soma_impares += i

    print(soma_impares)
