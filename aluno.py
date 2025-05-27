import functools

class Aluno:

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f'{self.nome}: {self.nota}'

def comparar_alunos(a, b):
    return (b.nota > a.nota) - (b.nota < a.nota)

# Criando a lista de alunos a partir da entrada do usuário
alunos = []
for _ in range(3):
    nome = input("Informe o nome do aluno: ")
    nota = float(input(f"Informe a nota de {nome}: "))
    alunos.append(Aluno(nome, nota))

# Ordenando a lista em ordem decrescente
alunos_ordenados = sorted(alunos, key=functools.cmp_to_key(comparar_alunos))

# Exibindo a lista ordenada
print("\nLista de alunos ordenada por nota:")
for aluno in alunos_ordenados:
    print(aluno)
