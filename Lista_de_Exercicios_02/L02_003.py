nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
media=(nota1 + nota2)/2
print("A média Aritmética de", nota1,"e",nota2,"é:",media)
if media >= 7:
   print("Aluno aprovado!")
else:
   print("Aluno reprovado!")