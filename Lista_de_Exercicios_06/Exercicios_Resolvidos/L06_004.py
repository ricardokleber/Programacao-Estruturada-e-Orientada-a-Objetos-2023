mat = []
l_maior = 0
c_maior = 0
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Informe o elemento [{i}][{j}]: "))
        if i == 0 and j == 0:
            maior = num
        linha.append(num)
        if num > maior:
            maior = num
            l_maior = i
            c_maior = j
    mat.append(linha)

for i in range(3):
    print(mat[i])

print(f"O maior número da matriz é: {maior} e está na posição [{l_maior}][{c_maior}]")