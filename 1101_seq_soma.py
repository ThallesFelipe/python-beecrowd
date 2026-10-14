m, n = map(int, (input().split()))

while m > 0 and n > 0:
    if m > n:
        m, n = n, m

    soma = 0

    for i in range(m, n + 1):
        print(i, end=" ")
        soma += i

    print(f"Sum={soma}")

    m, n = map(int, (input().split()))
