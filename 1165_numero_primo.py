def eh_primo(x: int) -> bool:
    if x < 2:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True


n: int = int(input())

for _ in range(n):
    x: int = int(input())

    if eh_primo(x):
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
