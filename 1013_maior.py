a, b, c = map(int, input().split())

maior_ab = int((a + b + abs(a - b)) / 2)
maior_final = int((maior_ab + c + abs(maior_ab - c)) / 2)

print(f"{maior_final} eh o maior")
