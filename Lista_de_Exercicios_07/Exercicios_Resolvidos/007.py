abastecimentos = {}
apurado = 0.00
qtd_etanol = 0.00
qtd_gasolina = 0.00
qtd_diesel = 0.00
while True:
    print("***** Posto Roberto Carlos ******")
    print(f"Valor Apurado no DIA: R$ {apurado:.2f}")
    print("*********************************")
    print("Registrar Abastecimento:")
    placa = input("Digite a placa do veículo ou 0 para finalizar: ")
    if placa == '0':
        break
    combustivel = input(f"[{placa}] Combustível (etanol|gasolina|diesel): ")
    if combustivel != 'etanol' and combustivel != 'gasolina' and combustivel != 'diesel':
        print("Informação Errada!!! Encerrando Sistema!!!")
        break
    litros = float(input(f"[{placa}] Quantidade de {combustivel} abastecida: "))
    abastecimentos.update({placa:[combustivel,litros]})
    if combustivel == 'etanol':
        apurado += litros*5
        qtd_etanol += litros
    elif combustivel == 'gasolina':
        apurado += litros*6
        qtd_gasolina += litros
    else:
        apurado += litros*5.5
        qtd_diesel += litros
print(f"Quantidade de Carros Atendidos: {len(abastecimentos)}")
print(f"Quantidade de litros de etanol vendidos: {qtd_etanol}")
print(f"Quantidade de litros de gasolina vendidos: {qtd_gasolina}")
print(f"Quantidade de litros de diesel vendidos: {qtd_diesel}")
print(f"Total Apurado no Dia: {apurado}")