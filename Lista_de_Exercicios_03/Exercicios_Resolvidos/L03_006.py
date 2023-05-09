nome = input("Insira seu nome (com pelo menos 3 caracteres): ")
cont = len(nome)
while cont <= 3:
   nome = input("Erro! Insira seu nome (com pelo menos 3 caracteres): ")
   cont = len(nome)
idade = int(input("Idade (entre 10 e 100): "))
while idade<10 or idade>100:
   idade = int(input("Erro! Idade (entre 10 e 100): "))
estado = input("Estado civil ('S' (solteiro), ‘C' (casado), 'V'(viúvo), 'D'(divorciado)): ")
while estado != 'S' and estado != 'C' and estado != 'V' and estado != 'D':
   estado = input("Erro! Estado civil ('S' (solteiro), ‘C' (casado), 'V'(viúvo), 'D'(divorciado)): ")
if estado == 'S':
   estado = "Solteiro"
elif estado == 'C':
   estado = "Casado"
elif estado == 'V':
   estado = "Viúvo"
elif estado == 'D':
   estado = "Divorciado"
telefone = input("Insira seu telefone (com 9 dígitos): ")
cont = len(telefone)
while cont != 9:
   telefone = input("Erro! Insira seu telefone (com 9 dígitos): ")
   cont = len(telefone)
print("Nome:",nome)
print("Idade:",idade)
print("Estado Civil:",estado)
print("Telefone:",telefone)
