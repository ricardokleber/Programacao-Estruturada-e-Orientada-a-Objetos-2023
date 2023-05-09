soma = 0
num = float(input("digite um número (ou zero para finalizar): "))
quant = 1
while num != 0:
   soma += num
   num = float(input("digite um número (ou zero para finalizar): "))
   quant += 1
media = soma /quant
print("A soma dos números digitados é: ", soma)
print("Cálculo da média: ",soma,"/",quant)
print("A média aritmética entre os números digitados é: ", media)
