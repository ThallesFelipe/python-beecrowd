x: int = int(input())

while x != 0:
    soma_consecutivo = 0

    for i in range(x, x + 5 * 2):
        if i % 2 == 0:
            soma_consecutivo += i

    print(soma_consecutivo)

    x = int(input())
