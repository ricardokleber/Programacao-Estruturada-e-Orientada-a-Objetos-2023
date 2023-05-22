mat = []
contador = 0
maiores = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input("Digite um número: "))
        linha.append(num)
        if num > 10:
            contador += 1
            maiores.append(num)
    mat.append(linha)
for i in mat:
    print(i)
print(f"{contador} números maiores que 10 = {maiores}")