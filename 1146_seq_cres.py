while True:
    x: int = int(input())

    if x == 0:
        break

    for i in range(1, x + 1):
        if not i == x:
            print(i, end=" ")
        else:
            print(i)
