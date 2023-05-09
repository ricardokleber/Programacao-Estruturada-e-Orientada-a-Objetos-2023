numeros = []
for i in range(5):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))
consulta = int(input("Digite um número para procurar na lista: "))
encontrado = 0
for busca in numeros:
    if busca == consulta:
        encontrado = 1
        break
if encontrado == 1:
    print(f"O número {consulta} está na lista!")
else:
    print(f"O número {consulta} não está na lista.")