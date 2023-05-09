numero = int(input("Digite um número: "))
if numero%2 == 0:
   classificacao = "par"
   resultado = numero**2
else:
   classificacao = "impar"
   resultado = numero**3
print(numero,"é",classificacao,"logo, o resultado é",resultado)