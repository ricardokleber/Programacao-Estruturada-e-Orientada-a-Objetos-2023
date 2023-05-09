lista = []
for i in range(5):
   lista.append(int(input("Digite um Número: ")))
for i in range(len(lista)):
   for j in range(i+1, len(lista)):
       if lista[i] > lista[j]:
           aux = lista [i]
           lista[i] = lista[j]
           lista[j] = aux
print(lista)
