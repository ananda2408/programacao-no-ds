class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros

    def adicionar_livro(self, titulo, autor, ano):
        livro = (titulo, autor, ano)  # Criando uma tupla com os dados do livro
        self.livros.append(livro)  # Adicionando automaticamente na lista

    def exibir_colecao(self):
        print("\nColeção de Livros:")
        for livro in self.livros:
            print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")

# Criando a biblioteca
biblioteca = Biblioteca()

# Adicionando livros à coleção
biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
biblioteca.adicionar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
biblioteca.adicionar_livro("1984", "George Orwell", 1949)

# Exibindo a coleção
biblioteca.exibir_colecao()
