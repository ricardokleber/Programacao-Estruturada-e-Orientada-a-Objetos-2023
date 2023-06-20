def main():
    while True:
        string = input("Digite uma String ou 'pare' para Sair: ")
        if string == 'pare':
            break
        else:
            print(trocavogal(string))

def trocavogal(string_original):
    string = string_original.upper()
    string = string.replace('A', '@').replace('E', '&').replace('I', '/').replace('O', '*').replace('U', '%')
    return string

if __name__ == '__main__':
    main()