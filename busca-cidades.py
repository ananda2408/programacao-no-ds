# Lista pré-definida de cidades
cidades = ["Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte", 
           "Porto Alegre", "Florianópolis", "Recife", "Salvador"]

# Solicita entrada do usuário
filtro = input("Digite uma letra ou sequência de caracteres para buscar nas cidades: ")

# Converte o filtro para minúsculas e filtra a lista
cidades_filtradas = [cidade for cidade in cidades if filtro.lower() in cidade.lower()]

# Exibe o resultado
if cidades_filtradas:
    print("\nCidades encontradas:")
    for cidade in cidades_filtradas:
        print(f"- {cidade}")
else:
    print("\nNenhuma cidade corresponde ao critério de busca.")
