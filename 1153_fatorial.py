def fatorial(n: int) -> int:
    if n == 0:
        return 1
    return n * fatorial(n - 1)


n = int(input())

print(fatorial(n))
