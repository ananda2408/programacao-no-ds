# Solicita o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Solicita o código de desconto
codigo = input("Digite o código de desconto (A, B ou C): ").upper()

# Aplica o desconto correspondente ao código
if codigo == 'A':
    desconto = 0.10  # 10% de desconto
elif codigo == 'B':
    desconto = 0.20  # 20% de desconto
elif codigo == 'C':
    desconto = 0.30  # 30% de desconto
else:
    desconto = 0  # Código inválido, sem desconto
    print("Código de desconto inválido!")

# Calcula o preço final
preco_final = preco * (1 - desconto)

# Exibe o preço final
print(f"O preço final do produto é: R$ {preco_final:.2f}")
