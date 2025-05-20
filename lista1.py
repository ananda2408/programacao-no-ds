# Solicita o número de elementos
n = int(input("Digite um número inteiro positivo: "))

# Inicializa a lista
lista = []

# Lê n números inteiros e os adiciona à lista
for _ in range(n):
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

# Solicita o número a ser verificado
x = int(input("Digite um número para verificar se está na lista: "))

# Verifica se x está na lista
if x in lista:
    print(f"{x} pertence à lista.")
else:
    print(f"{x} não pertence à lista.")
