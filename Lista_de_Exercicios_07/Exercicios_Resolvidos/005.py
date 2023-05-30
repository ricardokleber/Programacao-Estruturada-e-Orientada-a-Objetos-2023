alunos = {}

while True:
    matricula = int(input("Digite a Matrícula: "))
    if matricula == 0:
        break
    nome = input(f"[{matricula}] Digite o Nome: ")
    nota1 = float(input(f"[{matricula}] Nota 01 (entre 0 e 100): "))
    nota2 = float(input(f"[{matricula}] Nota 02 (entre 0 e 100): "))
    lista = [nome,nota1,nota2]
    alunos.update({matricula:lista})
print(f"Número de Alunos Matriculados: {len(alunos)}")
print("Nomes dos Alunos Matriculados: ")
notas1unidade = 0
notas2unidade = 0
for i in alunos.values():
    print(f"* {i[0]}")
    notas1unidade += i[1]
    notas2unidade += i[2]
print(f"Média das Notas da 1a Unidade: {notas1unidade/len(alunos)}")
print(f"Média das Notas da 2a Unidade: {notas2unidade/len(alunos)}")
print(f"Média Final da Turma: {(notas1unidade+notas2unidade)/(2*(len(alunos)))}")
print("Lista de Alunos Aprovados:")
for i in alunos.values():
    if (i[1]+i[2])/2 >= 60:
        print(f"* {i[0]}")
