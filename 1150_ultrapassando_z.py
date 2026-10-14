x = int(input())

z = float("-inf")

while z <= x:
    z = int(input())

soma = 0
qtd_iteracoes = 0

while soma < z:
    qtd_iteracoes += 1
    soma += x
    x += 1

print(qtd_iteracoes)
