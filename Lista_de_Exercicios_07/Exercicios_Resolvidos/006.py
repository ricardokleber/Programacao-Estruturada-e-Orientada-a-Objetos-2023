agenda = {}
while True:
    print("******** Agenda em Python *********")
    print(f"Existem: {len(agenda)} contatos cadastrados")
    print("***********************************")
    print("1. Inserir um contato")
    print("2. Consultar um contato")
    print("3. Remover um contato")
    print("4. Listar toda a agenda")
    print("0. Finalizar")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0:
        break
    elif opcao == 1:
        nome = input("Nome a Adicionar: ")
        telefone = input(f"Telefone de [{nome}]: ")
        email = input(f"E-Mail de [{nome}]: ")
        lista = [telefone,email]
        agenda.update({nome:lista})
    elif opcao == 2:
        consultar = input("Nome do Contato a Consultar: ")
        if consultar not in agenda.keys():
            print("Este contato não está na agenda!!!")
        else:
            print(f"{consultar} | Telefone: {agenda[consultar][0]} | E-Mail: {agenda[consultar][1]}")
    elif opcao == 3:
        remover = input("Nome do Contato a Remover: ")
        if remover not in agenda.keys():
            print("Este contato não está na agenda!!!")
        else:
            print(f"Contato [{remover}] Removido da Agenda!!!")
            agenda.pop(remover)
    elif opcao == 4:
        for nome,dados in agenda.items():
            print(f"{nome} | Telefone: {dados[0]} | E-Mail: {dados[1]}")
    else:
        print("Opção Inválida!!!")
