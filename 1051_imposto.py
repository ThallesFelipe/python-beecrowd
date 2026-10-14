renda = float(input())

if renda <= 2000:
    print("Isento")
else:
    imposto_renda = 0

    if renda <= 3000:
        imposto_renda = (renda - 2000) * 0.08

    elif renda <= 4500:
        imposto_renda = 1000 * 0.08
        imposto_renda += (renda - 3000) * 0.18

    else:
        imposto_renda = 1000 * 0.08
        imposto_renda += 1500 * 0.18
        imposto_renda += (renda - 4500) * 0.28

    print(f"R$ {imposto_renda:.2f}")
