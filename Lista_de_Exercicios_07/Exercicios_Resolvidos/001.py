agenda = []
for i in range(5):
    nome = input("Informe o nome a adicionar na agenda: ")
    telefone = input(f"Informe o telefone de [{nome}]: ")
    agenda.append({nome:telefone})
for i in range(5):
    print(agenda[i])
