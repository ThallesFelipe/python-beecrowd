def ler_nota() -> float:
    while True:
        nota: float = float(input())

        if 0 <= nota <= 10:
            return nota

        print("nota invalida")


while True:
    nota1: float = ler_nota()
    nota2: float = ler_nota()

    media: float = (nota1 + nota2) / 2

    print(f"media = {media:.2f}")

    cond: int = int(input("novo calculo (1-sim 2-nao)"))

    if cond == 2:
        break
