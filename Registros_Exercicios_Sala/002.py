agenda = {
    "Maria" :   34567890,
    "Jose"  :   43434343,
    "Ana"   :   12345678
}

print("Nomes Ordenados:")
for telefones in sorted(agenda.keys()):
    print(telefones)

print("Telefones Ordenados:")
for telefones in sorted(agenda.values()):
    print(telefones)

print("Registros Ordenados:")
for telefones in sorted(agenda.items()):
    print(telefones)

print("Registros Ordenados (Formatados):")
for nome,tel in sorted(agenda.items()):
    print(f"{nome} => Telefone: {tel}")