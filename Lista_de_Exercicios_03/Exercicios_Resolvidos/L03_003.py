num = int(input("digite um número para saber o seu fatorial: "))
cont = 1
fatorial = num
while cont != num:
   num -= 1
   fatorial = fatorial * num
print("O fatorial desse número é:", fatorial)
