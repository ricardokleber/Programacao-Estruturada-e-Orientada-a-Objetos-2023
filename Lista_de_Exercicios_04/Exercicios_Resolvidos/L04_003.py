listanormal = []
for i in range(10):
   listanormal.append(int(input("Digite um Número Inteiro: ")))
listainvertida = []
for i in range(9,-1,-1):
   listainvertida.append(listanormal[i])
print("Lista Normal", listanormal)
print("Lista Invertida", listainvertida)
