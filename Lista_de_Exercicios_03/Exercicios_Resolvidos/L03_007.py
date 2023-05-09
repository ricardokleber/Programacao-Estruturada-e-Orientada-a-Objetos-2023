num = int(input("Digite um número ou 0 para finalizar: "))
par = 0
impar = 0
if num % 2 == 0:
   par += num
else:
   impar += num
while num != 0:
   num = int(input("Digite um número ou 0 para finalizar: "))
   if num % 2 == 0:
       par += num
   else:
       impar += num
print ("Soma dos números pares: ", par)
print ("Soma dos números ímpares: ", impar)
