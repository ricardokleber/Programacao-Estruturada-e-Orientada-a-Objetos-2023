nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
if media >= 7 :
   print("Média Final: ",media," = Aluno Aprovado!")
elif media < 4 :
   print("Média Final: ",media," = Aluno Reprovado!")
else :
  print("Média Parcial: ",media," = Aluno em Recuperação")
  nota_rec = float(input("Digite a nota da recuperação: "))
  media_final = (media + nota_rec)/2
  print("Média Final do Aluno após Recuperação:", media_final)