codigo, quantidade = map(int, input().split())

catalogo = [(1, 4.00), (2, 4.50), (3, 5.00), (4, 2.00), (5, 1.50)]

for item, preco in catalogo:
    if codigo == item:
        total = preco * quantidade
        print(f"Total: R$ {total:.2f}")
        break