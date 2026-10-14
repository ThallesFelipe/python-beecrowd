valor = float(input())

intervalos = [
    (0, 25, "[0,25]"),
    (25, 50, "(25,50]"),
    (50, 75, "(50,75]"),
    (75, 100, "(75,100]"),
]

achou = False

for inicio, fim, texto in intervalos:
    if inicio == 0:
        if valor >= inicio and valor <= fim:
            print(f"Intervalo {texto}")
            achou = True
            break
    else:
        if valor > inicio and valor <= fim:
            print(f"Intervalo {texto}")
            achou = True
            break

if not achou:
    print("Fora de intervalo")
