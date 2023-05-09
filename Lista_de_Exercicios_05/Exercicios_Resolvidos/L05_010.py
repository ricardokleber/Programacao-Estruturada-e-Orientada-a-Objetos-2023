lista1 = []
lista2 = []
print("Informe os elementos da primeira lista:")
for i in range(5):
    lista1.append(input(f"Elemento {i+1}: "))
print("Informe os elementos da segunda lista:")
for i in range(5):
    lista2.append(input(f"Elemento {i+1}: "))
lista3 = []
for i in lista1+lista2:
    if i not in lista3:
        lista3.append(i)
lista3.sort()
print(lista3)