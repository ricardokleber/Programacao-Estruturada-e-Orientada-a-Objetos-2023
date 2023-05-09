notas = []
notas.append(float(input("Primeira Nota: ")))
notas.append(float(input("Segunda Nota: ")))
notas.append(float(input("Terceira Nota: ")))
notas.append(float(input("Quarta Nota: ")))
soma = 0
for nota in notas:
   soma += nota
media = soma / len(notas)
maior = notas[0]
for nota in notas:
   if nota > maior:
       maior = nota
menor = notas[0]
for nota in notas:
   if nota < menor:
       menor = nota
print("Média aritmética:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)