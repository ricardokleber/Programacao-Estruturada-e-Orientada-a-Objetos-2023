agenda = {
    "chico@gmail.com" : "Chico",
    "maria@gmail.com" : "Maria",
    "gorete@gmail.com" : "Gorete"        
}

busca = input("Qual o E-Mail da Pessoa Procurada? ")

if busca in agenda.keys():
    print(f"O E-mail {busca} pertence a {agenda[busca]}")
else:
    print("Cadastro Não Encontrado!")