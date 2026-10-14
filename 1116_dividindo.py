n: int = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    if y == 0:
        print("divisao impossivel")
    else:
        print(round(x / y, 1))
