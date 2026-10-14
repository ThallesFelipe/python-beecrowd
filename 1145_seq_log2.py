x, y = map(int, input().split())

i = 1

while i != y + 1:
    if not i % x == 0:
        print(i, end=" ")
        i += 1
    else:
        print(i)
        i += 1
