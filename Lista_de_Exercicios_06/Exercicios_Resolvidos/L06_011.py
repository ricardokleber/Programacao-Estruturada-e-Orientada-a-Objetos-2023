vogais = [
    ['A','0','0','0','0'],
    ['0','E','0','0','0'],
    ['0','0','I','0','0'],
    ['0','0','0','O','0'],
    ['0','0','0','0','U'],
]
consoantes = [
    ['B','C','D','F','G'],
    ['H','J','K','L','M'],
    ['N','P','Q','R','S'],
    ['T','V','W','X','Y'],
    ['Z','0','0','0','0'],
]
nome_string = 'RICARDO'
nome_lista = []

for letra in nome_string:
    for i in range(5):
        for j in range(5):
            if letra == vogais[i][j]:
                nome_lista.append(vogais[i][j])
            if letra == consoantes[i][j]:
                nome_lista.append(consoantes[i][j])
print(nome_lista)
