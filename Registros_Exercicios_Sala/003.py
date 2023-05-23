alunos = {111111 : ['João Maria','joao@gmail.com','99999-1111'],
         222222 : ['Chico Lopes','chico@gmail.com','98888-2222']}

busca = int(input("Matrícula do Aluno a Procurar: "))
if busca in alunos:
   dados_aluno = alunos[busca]
   print(f"Matrícula: {busca}")
   print(f"Nome do Aluno: {dados_aluno[0]}") # primeiro valor da lista
   print(f"E-Mail: {dados_aluno[1]}") # segundo valor da lista
   print(f"Telefone: {dados_aluno[2]}") # terceiro valor da lista
else:
   print("Não Existe Aluno Cadastrado com a Matrícula Informada")
