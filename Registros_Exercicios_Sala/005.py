# Agenda
# Índice = Nome
# Campos = Telefone e E-Mail

agenda = dict()

while True:
    nome = input("Digite o Nome a acrescentar (ou 0 para sair): ")
    if nome == "0":
        break
    telefone = input(f"Telefone de [{nome}]: ")
    email = input(f"E-Mail de [{nome}]: ")
    campos = [telefone,email]
    agenda[nome] = campos
    for x,y in agenda.items():
            print(f"{x}|{y[0]}|{y[1]}")