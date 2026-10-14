n = int(input())

seq = [0, 1]

for _ in range(n - 2):
    seq.append(seq[-1] + seq[-2])

print(*seq[:n])
