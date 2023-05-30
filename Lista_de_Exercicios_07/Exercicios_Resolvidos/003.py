produtos = {}
for i in range(5):
    codigo = int(input("Digite o Código do Produto: "))
    nome = input("Digite o Nome do Produto: ")   
    preco = float(input(f"Preço de [{nome}]: "))
    quantidade = float(input(f"Quantidade de [{nome}]: "))
    lista = [nome,preco,quantidade]
    produtos.update({codigo:lista})
print("===== Relatório =====")
print("Produtos Disponíveis: ")
itens = 0
valorestoque = 0
for nomes in produtos.values():
    print (f"* {nomes[0]}")
    itens += nomes[2]
    temp = nomes[1]*nomes[2]
    valorestoque += temp
print(f"Quantidade Total de Itens: {itens}")
print(f"Valor total do estoque: R$ {valorestoque}")