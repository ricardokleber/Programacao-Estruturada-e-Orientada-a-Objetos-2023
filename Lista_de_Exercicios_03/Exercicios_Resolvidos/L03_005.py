dep_inicial = float(input("Depósito inicial: "))
juros = float(input("Taxa de juros mensal: "))
mes = 0
val_juros = dep_inicial
while mes != 12:
   val_juros = val_juros + (val_juros * (juros/100))
   mes += 1
   print("No mês",mes,"o valor atualizado é/foi: ", val_juros)
print("Total de Juros Recebidos: ",val_juros - dep_inicial)
