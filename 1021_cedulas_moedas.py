valor = float(input())
centavos = round(valor * 100)

notas = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
for nota in notas:
    quantidade_notas = centavos // nota
    centavos %= nota

    print(f"{quantidade_notas} nota(s) de R$ {nota}.00")

moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("MOEDAS:")
for moeda in moedas:
    quantidade_moedas = centavos // moeda
    centavos = centavos % moeda

    print(f"{quantidade_moedas} moeda(s) de R$ {moeda:.2f}")
