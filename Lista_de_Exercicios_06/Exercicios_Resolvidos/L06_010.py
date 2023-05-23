nome = input("Digite uma palavra qualquer: ")
lista_nome = []
for i in range(len(nome)):
    lista_nome.append(nome[i])
matriz = []
indice_lista = 0
for i in range(4):
    linha = []
    for j in range(4):
        if indice_lista < len(nome):
            linha.append(lista_nome[indice_lista])
            indice_lista += 1
        else:
            linha.append('X')
    matriz.append(linha)

for i in range(4):
    print("| ", end = "")
    for j in range(4):
        print(matriz[i][j], end = " ")
    print("|")