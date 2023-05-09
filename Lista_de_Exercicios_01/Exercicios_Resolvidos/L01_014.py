valor_original = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
desconto = valor_original * percentual_desconto / 100
print("Valor a Pagar :", valor_original - desconto)