m = []
for i in range(3):
    linha = []
    for j in range(3):
        caractere = input(f"Digite a LETRA para posição [{i}][{j}]: ")
        linha.append(caractere)
    m.append(linha)
for i in m:
    print(i)
lista = []
for i in range(3):
    for j in range(3):
        if i == j:
            lista.append(m[i][j])
print(f"Lista (Elementos da Diagonal Principal) = {lista}")