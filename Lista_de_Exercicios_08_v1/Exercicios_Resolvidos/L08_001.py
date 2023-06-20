def main():
    while True:
        print('''
        ======================
        [1] Adicionar Registro
        [2] Apagar Registro
        [3] Listar Amigos
        [0] Sair
        ======================''')
        opcao = int(input('Digite sua Opção: '))
        if opcao == 0:
            break
        elif opcao == 1:
            adicionar()
        elif opcao == 2:
            apagar()
        elif opcao == 3:
            listar()

def adicionar():
    cpf = int(input('CPF: '))
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    arquivo = open('agenda.txt','a')
    arquivo.write(f'{cpf}:{nome},{telefone}\n')
    arquivo.close()

def converte_arq_dict():
    dicionario = {}
    arquivo = open('agenda.txt','r')
    registros = arquivo.readlines()
    arquivo.close()
    for i in range(len(registros)):
        cpf = int(registros[i].split(':')[0])
        lista = registros[i].split(':')[1]
        lista1 = lista.replace('\n','')
        nome = lista1.split(',')[0]
        telefone = lista1.split(',')[1]
        dicionario[cpf] = [nome,telefone]
    return dicionario    

def listar():
    agenda = converte_arq_dict()
    for cpf,lista in agenda.items():
        print(f'CPF: {cpf} | Nome: {lista[0]} | Telefone: {lista[1]}')

def apagar():
    cpf = int(input('CPF do Registro a Apagar: '))
    agenda = converte_arq_dict()
    if cpf not in agenda.keys():
        print(f'CPF [{cpf}] Não Cadastrado!!!')
    else:
        agenda.pop(cpf)
        arquivo = open('agenda.txt','w')
        arquivo.close()
        for cpf,lista in agenda.items():
            arquivo = open('agenda.txt','a')            
            arquivo.writelines(f'{cpf}:{lista[0]},{lista[1]}\n')
        arquivo.close()

if __name__ == '__main__':
    main()