string_consulta = input("Digite uma string: ")
string_consulta = string_consulta
contador = 0
condition = False

for caracter in string_consulta:
    for caracter_teste in string_consulta:
        if caracter == caracter_teste:
            contador += 1
            
    print(f"O caractere {caracter} apareceu {contador} vez(es) na strig")
    contador = 0
