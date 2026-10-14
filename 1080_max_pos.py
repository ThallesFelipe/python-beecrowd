QTD = 100
pos, max = 0, 0
for i in range(QTD):
    val = int(input())

    if val > max:
        max = val
        pos = i + 1

print(max)
print(pos)
