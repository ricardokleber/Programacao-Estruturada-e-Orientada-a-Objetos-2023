mat = []
for i in range(4):
    linha = []
    for j in range(4): 
        linha.append((i)*(j))
    mat.append(linha)
for i in mat:
    print(i)