# Lista de alunos com nome e nota
alunos = [
    {"nome": "Carlos", "nota": 85},
    {"nome": "Ana", "nota": 92},
    {"nome": "Bruno", "nota": 78},
    {"nome": "Débora", "nota": 90}
]

# Ordenando por nome (modifica diretamente a lista)
alunos.sort(key=lambda aluno: aluno["nome"])

print("Alunos ordenados por nome:")
for aluno in alunos:
    print(aluno)

# Ordenando por nota em ordem decrescente (gera uma nova lista)
alunos_por_nota = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)

print("\nAlunos ordenados por nota (decrescente):")
for aluno in alunos_por_nota:
    print(aluno)
