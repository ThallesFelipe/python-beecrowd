dias_vida = int(input())

anos, dias_vida = divmod(dias_vida, 365)
meses, dias_vida = divmod(dias_vida, 30)

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias_vida} dia(s)")
