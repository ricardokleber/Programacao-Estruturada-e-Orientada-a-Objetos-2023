p1 = float(input("Qual o Preço do Primeiro Produto? "))
p2 = float(input("Qual o Preço do Segundo Produto? "))
p3 = float(input("Qual o Preço do Terceiro Produto? "))
if p1 < p2 and p1 < p3 :
   menor = p1
   compra = "Primeiro"
elif p2 < p1 and p2 < p3:
   menor = p2
   compra = "Segundo"
else:
   menor = p3
   compra = "Terceiro"
print("Você deve comprar o",compra,"Produto, que custa R$",menor)