linhas = int(input("Número de Linhas da Matriz A: "))
colunas = int(input("Número de Colunas da Matriz A: "))
mat_a = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        num = int(input(f"Digite o elemento[{i}][{j}]: "))
        linha.append(num)
    mat_a.append(linha)
print("Matriz A:")
for i in mat_a:
    print(i)
mat_b = []
for linhas2 in range(colunas):
    linha = []
    for colunas2 in range(linhas):
        linha.append(mat_a[colunas2][linhas2])
    mat_b.append(linha)
print("Matriz B:")
for linhas2 in mat_b:
    print(linhas2)