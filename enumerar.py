# Solicita ao usuário que insira os nomes, separados por vírgula
nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")

# Remove espaços extras dos nomes
nomes = [nome.strip() for nome in nomes]

# Itera sobre a lista usando a função enumerate e exibe os resultados
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")
