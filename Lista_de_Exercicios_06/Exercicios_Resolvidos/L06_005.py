A = []
B = []
C = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o Elemento [{i}][{j}] da 1a Matriz: "))
        linha.append(num)
    A.append(linha)

for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o Elemento [{i}][{j}] da 2a Matriz: "))
        linha.append(num)
    B.append(linha)

for i in range(3):
    linha = []
    for j in range(3):
        if A[i][j] > B[i][j]:
            linha.append(A[i][j])
        else:
            linha.append(B[i][j])
    C.append(linha)

for i in C:
    print(i)