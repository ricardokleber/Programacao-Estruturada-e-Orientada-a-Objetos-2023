lista = []
while True:
   num = int(input("Digite um número inteiro ou 0 para sair: "))
   if num == 0:
       break
   lista.append(num)
num_str = ""
for numeros in lista:
   num_str += str(numeros)
print(num_str)