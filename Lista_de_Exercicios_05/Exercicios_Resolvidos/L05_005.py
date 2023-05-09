frase = input("Digite uma frase: ")
frase = frase.replace('.',' ').replace(',',' ').replace('?',' ').replace(';',' ').replace(':',' ').replace('!',' ')
frase = frase.split()
num_palavras = 0
for i in frase:
    num_palavras += 1
print(f"A frase tem {num_palavras} palavras")
