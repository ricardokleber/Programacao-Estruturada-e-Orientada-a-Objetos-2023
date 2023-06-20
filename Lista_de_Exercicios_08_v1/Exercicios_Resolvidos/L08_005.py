from datetime import date

def main():
    calculaidade(input('Informe sua data de nascimento no formato DD/MM/AAAA: '))

def calculaidade(idade):
    dia_hoje = date.today().day
    mes_hoje = date.today().month
    ano_hoje = date.today().year
    dia = idade.split('/')[0]
    mes = idade.split('/')[1]
    ano = idade.split('/')[2]
    anos = int(ano_hoje) - int(ano)
    if int(mes_hoje) < int(mes):
            anos -= 1
    elif int(mes_hoje) == int(mes):
        if int(dia_hoje) <= int(dia):
            anos -= 1
    print(f"Sua Idade Hoje [{dia}/{mes}/{ano}] é {anos} anos")

if __name__ == '__main__':
    main()
