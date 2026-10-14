n = int(input())

P1 = 2
P2 = 3
P3 = 5

for _ in range(n):
    n1, n2, n3 = map(float, input().split())

    print(f"{(n1 * P1 + n2 * P2 + n3 * P3) / (P1 + P2 + P3):.1f}")
