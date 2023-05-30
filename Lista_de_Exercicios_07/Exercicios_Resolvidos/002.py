aprovados = {}
reprovados = {}
while True:
    aluno = input("Digite o nome do Aluno a inserir: ")
    if aluno == 'pare':
        break
    media = float(input(f"Digite a média de [{aluno}] (de 0 a 100): "))
    if media >= 60:
        aprovados.update({aluno:media})
    else:
        reprovados.update({aluno:media})
print("Alunos Aprovados:")
for i in aprovados.keys():
    print(i)
print("Alunos Reprovados:")
for i in reprovados.keys():
    print(i)
