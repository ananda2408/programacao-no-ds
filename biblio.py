class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: '{self.titulo}'\nAutor: {self.autor}\nPáginas: {self.paginas}"

# Solicitando os dados do livro ao usuário
titulo = input("Digite o título do livro: ")
autor = input("Digite o nome do autor: ")
paginas = input("Digite a quantidade de páginas: ")

# Criando um objeto da classe Livro
livro = Livro(titulo, autor, paginas)

# Exibindo a descrição formatada do livro
print("\nDados do livro cadastrado:")
print(livro)
