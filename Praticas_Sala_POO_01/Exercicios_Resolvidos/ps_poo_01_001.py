from eletrodomesticos import Televisao

def main():
    tv_sala = Televisao()
    tv_sala.nome = 'tv_sala'
    tv_sala.tamanho = 32
    tv_sala.marca = 'Filipys'

    tv_quarto = Televisao()
    tv_quarto.nome = 'tv_quarto'
    tv_quarto.marca = 'Xilco'
    tv_quarto.ligada = True

    lista_tvs = [tv_sala,tv_quarto]

    for tvs in lista_tvs:
        if tvs.ligada:
            ligada = 'S'
        else:
            ligada = 'N'
        print(f'{tvs.nome} | {tvs.canal} | {tvs.tamanho} | {tvs.marca} | {ligada}')    





if __name__ == '__main__':
    main()