nome = input("Qual o seu nome? ")
turno = input('Em que turno você estuda? Digite M para matutino e V para vespertino: ')
if turno == "M" :
   print("Bom dia,", nome)
elif turno == "V" :
   print("Boa tarde,", nome)
else :
   print("O turno digitado não é uma opção válida!!!")