PESO_A = 2
PESO_B = 3
PESO_C = 5

PESO_TOTAL = PESO_A + PESO_B + PESO_C

nota_a = float(input()) * PESO_A
nota_b = float(input()) * PESO_B
nota_c = float(input()) * PESO_C

media = (nota_a + nota_b + nota_c) / PESO_TOTAL
print(f"MEDIA = {media:.1f}")
