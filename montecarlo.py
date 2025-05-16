import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
anos = 10
simulacoes = 10  # Ajuste para melhor visualização do gráfico
retorno_medio_anual = 0.07
desvio_padrao_anual = 0.20
valor_inicial = 10000  # Valor inicial da carteira

# Criando um array para armazenar os valores simulados
trajetorias = np.zeros((simulacoes, anos + 1))
trajetorias[:, 0] = valor_inicial  # Define o valor inicial para todas as simulações

# Simulação de Monte Carlo
for i in range(simulacoes):
    for j in range(1, anos + 1):
        retorno_anual = np.random.normal(retorno_medio_anual, desvio_padrao_anual)
        trajetorias[i, j] = trajetorias[i, j - 1] * (1 + retorno_anual)

# Plotando os resultados
plt.figure(figsize=(10, 6))
for i in range(simulacoes):
    plt.plot(range(anos + 1), trajetorias[i], alpha=0.7)

plt.xlabel("Anos")
plt.ylabel("Valor da Carteira")
plt.title("Simulação de Monte Carlo: Trajetórias da Carteira de Investimentos")
plt.grid(True)
plt.show()
