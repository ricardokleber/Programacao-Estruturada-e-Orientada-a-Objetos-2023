numero = int(input("Digite um número: "))
numero = str(numero)
if numero == numero[::-1]:
    print("Palíndromo.")
else:
    print("Não é palíndromo")