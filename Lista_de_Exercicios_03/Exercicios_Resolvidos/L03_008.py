numero = 1
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
while numero != 0:
   numero = int(input("Insira um número entre 1 e 100 ou 0 para finalizar: "))
   if 1 <= numero <= 25:
       intervalo1 += 1
   elif 26 <= numero <= 50:
       intervalo2 += 1
   elif 51 <= numero <= 75:
       intervalo3 += 1
   elif 76 <= numero <= 100:
       intervalo4 += 1
print ("Quantidade de números no intervalo de 1-25: ", intervalo1)
print ("Quantidade de números no intervalo de 26-50: ", intervalo2)
print ("Quantidade de números no intervalo de 51-75: ", intervalo3)
print ("Quantidade de números no intervalo de 76-100: ", intervalo4)