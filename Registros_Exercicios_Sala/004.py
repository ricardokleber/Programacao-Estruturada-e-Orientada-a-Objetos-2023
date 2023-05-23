produtos = {1: ['Monitor LED 24"', 599.99, 1],
           2: ['Teclado wireless', 49.26, 1],
           3: ['Mouse wireless', 19.9, 1],
           4: ['Cartucho colorido', 54, 2]}
total = 0
for prod in produtos.values():
    subtotal = prod[1] * prod[2]
    print(f"{prod[0]}: R$ {subtotal:.2f}")
    total += subtotal
print(30 * "-")
print(f"Total: R$ {total:.2f}")
