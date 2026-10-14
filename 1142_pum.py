n = int(input())
qtd_linhas = 0
i = 1

while qtd_linhas != n:
    if not i % 4 == 0:
        print(i, end=" ")
        i += 1
    else:
        print("PUM")
        qtd_linhas += 1
        i += 1
