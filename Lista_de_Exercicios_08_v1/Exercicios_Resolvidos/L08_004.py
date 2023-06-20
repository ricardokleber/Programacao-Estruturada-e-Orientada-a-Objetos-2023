def main():
    dataporextenso(input('Informe a Data no formato DD/MM: '))

def dataporextenso(data):
    dia = int(data.split('/')[0])
    mes = int(data.split('/')[1])

    dias = [
        'PRIMEIRO','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ',
        'ONZE','DOZE','TREZE','CATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO',
        'DEZENOVE','VINTE','VINTE E UM','VINTE E DOIS','VINTE E TRÊS','VINTE E QUATRO',
        'VINTE E CINCO','VINTE E SEIS','VINTE E SETE','VINTE E OITO','VINTE E NOVE',
        'TRINTA','TRINTA E UM'
        ]

    meses = [
        'JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO',
        'JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO'
        ]

    print(f'{dias[dia-1]} DE {meses[mes-1]}')

if __name__ == '__main__':
    main()