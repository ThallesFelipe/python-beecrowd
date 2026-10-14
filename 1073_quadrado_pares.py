n = int(input())

if not (n <= 5 or n >= 2000):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i}^2 = {i**2}")
