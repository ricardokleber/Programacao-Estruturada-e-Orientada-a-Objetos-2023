certo = 35
tentativa = 0
while certo != tentativa:
   tentativa = int(input("Digite um número inteiro: "))
   if tentativa != certo:
       print("Errou. Você não está com sorte!")
print("Parabéns! Você acertou o número sorteado.")
