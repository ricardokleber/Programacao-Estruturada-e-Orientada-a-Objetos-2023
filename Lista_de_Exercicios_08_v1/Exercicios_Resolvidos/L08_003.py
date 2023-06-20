import random
import string

def cria_senha(tamanho):
    caracteres = string.ascii_letters + string.digits
    senha = ''
    for i in range(tamanho):
        senha = senha+(random.choice(caracteres))
    return senha

def main():
    tam_da_senha = int(input("Tamanho da senha: "))
    n_senhas = int(input("Quantidade de senhas: "))
    arquivo = open('senhas.txt','a')
    for i in range(n_senhas):
        senha = cria_senha(tam_da_senha)
        arquivo.writelines(senha + '\n')
    arquivo.close()

if __name__ == '__main__':
    main()
