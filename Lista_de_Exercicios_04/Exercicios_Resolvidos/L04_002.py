num = []
num.append(int(input("Digite um Número Inteiro: ")))
maior = num[0]
menor = num[0]
pos_maior = 0
pos_menor = 0
for i in range(1,5):
   num.append(int(input("Digite um Número Inteiro: ")))
   if num[i] > maior :
       maior = num[i]
       pos_maior = i
   if num[i] < menor :
       menor = num[i] 
       pos_menor = i
print(num)
print("Maior Número",maior,"posição",pos_maior)
print("Menor Número",menor,"posição",pos_menor)