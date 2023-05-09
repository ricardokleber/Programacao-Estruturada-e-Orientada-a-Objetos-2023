print("Você deve inserir dois números sendo o segundo maior que o primeiro")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0
while num1 < num2 :
   num1 += 1
   if num1 % 2 == 0 and num1 != num2 :
       soma += num1
print("A soma dos números pares entre eles é: ", soma)
