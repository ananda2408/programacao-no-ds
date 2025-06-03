class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def registrar(self):
        return f"Animal registrado: {self.nome} ({self.especie})"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro")
        self.raca = raca

    def registrar(self):
        return f"Cachorro registrado: {self.nome}, Raça: {self.raca}"

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, "Gato")
        self.cor = cor

    def registrar(self):
        return f"Gato registrado: {self.nome}, Cor: {self.cor}"

# Exemplo de uso
animais = [
    Cachorro("Rex", "Labrador"),
    Gato("Mimi", "Preto"),
    Animal("Pérola", "Papagaio")
]

for animal in animais:
    print(animal.registrar())
