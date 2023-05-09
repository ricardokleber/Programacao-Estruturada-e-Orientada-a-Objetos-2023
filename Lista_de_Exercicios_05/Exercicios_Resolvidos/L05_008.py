nascimento = input("Digite a sua data de nascimento (dd/mm/aaaa): ")
campo = nascimento.split("/")
data = campo[0]
mes_numero = int(campo[1])-1
ano = campo[2]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print(f"{data} de {meses[mes_numero]} de {ano}")