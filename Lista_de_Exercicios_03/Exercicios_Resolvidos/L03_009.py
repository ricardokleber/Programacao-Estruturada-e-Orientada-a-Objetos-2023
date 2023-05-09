saldo = 1000
while saldo > 0:
 compras = float(input("Digite o valor das compras: "))
 if compras > saldo:
   print("Não há Saldo suficiente para esta compra!!!")
 else:
   saldo -= compras
 print("Saldo atual: ",saldo)
