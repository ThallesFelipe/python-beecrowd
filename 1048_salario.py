salario = float(input())

reajustes = [15, 12, 10, 7, 4]

if salario <= 400:
    novo_salario = salario + (salario * (reajustes[0] / 100))
    porcentagem = reajustes[0]
elif salario <= 800:
    novo_salario = salario + (salario * (reajustes[1] / 100))
    porcentagem = reajustes[1]
elif salario <= 1200:
    novo_salario = salario + (salario * (reajustes[2] / 100))
    porcentagem = reajustes[2]
elif salario <= 2000:
    novo_salario = salario + (salario * (reajustes[3] / 100))
    porcentagem = reajustes[3]
else:
    novo_salario = salario + (salario * (reajustes[4] / 100))
    porcentagem = reajustes[4]

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {(novo_salario - salario):.2f}")
print(f"Em percentual: {porcentagem} %")
