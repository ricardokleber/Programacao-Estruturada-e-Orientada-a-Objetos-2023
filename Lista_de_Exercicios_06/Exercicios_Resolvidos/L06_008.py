nome = input("Digite seu primeiro nome: ")
lista_nome = []
while len(lista_nome) < 17:
    for i in nome:
        if len(lista_nome) < 17:
            lista_nome.append(i)
matriz = []
indice_lista = 0
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(lista_nome[indice_lista])
        indice_lista += 1
    matriz.append(linha)

for i in range(4):
    print("| ", end = "")
    for j in range(4):
        print(matriz[i][j], end = " ")
    print("|")