num = int(input("Digite um número inteiro maior que 1000: "))
num_str = str(num)
num_inv = num_str[::-1]
num = int(num_inv)
print(f"Resultado: {num + 1000}")