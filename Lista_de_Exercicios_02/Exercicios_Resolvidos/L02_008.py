p1 = float(input("Informe a estatura da primeira pessoa: "))
p2 = float(input("Informe a estatura da segunda pessoa: "))
p3 = float(input("Informe a estatura da terceira pessoa: "))
if p1 == p2 or p1 == p3 or p2 == p3 :
   print("Há, pelo menos, duas pessoas com a mesma estatura")
else :
   if p1 > p2 and p1 > p3 :
       maior = p1
   elif p2 > p1 and p2 > p3:
       maior = p2
   else:
       maior = p3
   print("A pessoa de maior estatura tem",maior,"metros")
