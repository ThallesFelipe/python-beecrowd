n1, n2, n3, n4 = map(float, input().split())

PESOS = [2, 3, 4, 1]
PESO_TOTAL = sum(PESOS)

n1 *= PESOS[0]
n2 *= PESOS[1]
n3 *= PESOS[2]
n4 *= PESOS[3]

nota_media = (n1 + n2 + n3 + n4) / PESO_TOTAL

print(f"Media: {nota_media:.1f}")

if nota_media >= 7.0:
    print("Aluno aprovado.")
elif nota_media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    nota_final = (nota_exame + nota_media) / 2
    if nota_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado")
    print(f"Media final: {nota_final:.1f}")
