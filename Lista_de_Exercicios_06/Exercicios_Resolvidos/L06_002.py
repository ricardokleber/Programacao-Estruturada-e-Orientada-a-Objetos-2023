mat = []
maiores = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o Elemento [{i}][{j}]: "))
        linha.append(num)
        if num > 10:
            maiores.append(num)
    mat.append(linha)
for i in mat:
    print(i)
print(f"{len(maiores)} números maiores que 10 = {maiores}")