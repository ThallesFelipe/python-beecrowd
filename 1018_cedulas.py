quantidade_reais = int(input())

print(quantidade_reais)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade_notas = quantidade_reais // nota
    quantidade_reais = quantidade_reais % nota

    print(f"{quantidade_notas} nota(s) de R$ {nota},00")
