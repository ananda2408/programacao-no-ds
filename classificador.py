# Solicita um número ao usuário
numero = float(input("escreva um numero"))

# Verifica se o número é positivo
if numero > 0:
    # Se for positivo, imprime a mensagem
    print("O número é positivo.")
# Verifica se o número é negativo
elif numero < 0:
    # Se for negativo, imprime a mensagem
    print("o numero e negativo")
# Se não for positivo nem negativo, é zero
else:
    # Imprime a mensagem para zero
    print("o numero e igual a zero")
