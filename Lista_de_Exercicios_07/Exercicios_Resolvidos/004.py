registros = {
    'feijoada':0.00,
    'feijao_verde':0.00
}
while True:
    print("*********** Consumo de Feijão na Cantina ***********")
    print("Foram consumidos até o momento aproximadamente:")
    print(f"* {registros['feijoada']:.2f} quilos de Feijoada")
    print(f"* {registros['feijao_verde']:.2f} quilos de Feijão Verde")
    print("****************************************************")
    print("Digite:")
    print("1 para registrar a venda de um prato de Feijoada")
    print("2 para registrar a venda de um prato de Feijão Verde")
    escolha = int(input("Opção: "))
    if escolha != 1 and escolha != 2:
        break
    if escolha == 1:
        quantidade = registros['feijoada']
        registros.update({'feijoada':quantidade+0.20})
    else:
        quantidade = registros['feijao_verde']
        registros.update({'feijao_verde':quantidade+0.20})