n = int(input())

MIN = 10
MAX = 20
qtd_in = 0
qtd_out = 0

for i in range(n):
    x = int(input())

    if x >= MIN and x <= MAX:
        qtd_in += 1
    else:
        qtd_out += 1


print(f"{qtd_in} in")
print(f"{qtd_out} out")
