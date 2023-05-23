m =[]
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o Elemento [{i}][{j}]: "))
        linha.append(num)
    m.append(linha)
for i in range(3):
    for j in range(3):
        if i + j == 2:
            soma += m[i][j]
for i in m:
    print(i)
print(f"Soma dos elementos da diagonal secundária: {soma}")