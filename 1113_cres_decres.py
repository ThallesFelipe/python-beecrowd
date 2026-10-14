x, y = map(int, input().split())


def is_crescente(x: int, y: int) -> bool:
    return x < y


while not x == y:
    if is_crescente(x, y):
        print("Crescente")
    else:
        print("Decrescente")

    x, y = map(int, input().split())
