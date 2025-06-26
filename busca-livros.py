# Lista pré-definida de títulos de livros
livros = [
    "Cem Anos de Solidão",
    "O Senhor dos Anéis",
    "Dom Casmurro",
    "1984",
    "O Pequeno Príncipe",
    "Harry Potter e a Pedra Filosofal",
    "O Nome do Vento",
    "Orgulho e Preconceito",
    "A Revolução dos Bichos",
    "Capitães da Areia"
]

# Solicita ao usuário uma palavra-chave
busca = input("Digite uma palavra ou trecho para buscar nos títulos: ").lower()

# Filtra os títulos que contêm a palavra-chave (ignorando maiúsculas/minúsculas)
resultados = [livro for livro in livros if busca in livro.lower()]

# Exibe os resultados
if resultados:
    print("\nTítulos encontrados:")
    for titulo in resultados:
        print(f"- {titulo}")
else:
    print("\nNenhum título corresponde à sua busca.")
