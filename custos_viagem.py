class Veiculo:
    def __init__(self, nome, consumo):  # consumo em km por litro
        self.nome = nome
        self.consumo = consumo

    def calcular_custo(self, distancia, preco_combustivel):
        litros_necessarios = distancia / self.consumo
        return litros_necessarios * preco_combustivel

class Carro(Veiculo):
    def __init__(self, nome, consumo):
        super().__init__(nome, consumo)

class Moto(Veiculo):
    def __init__(self, nome, consumo):
        super().__init__(nome, consumo)

class Caminhao(Veiculo):
    def __init__(self, nome, consumo):
        super().__init__(nome, consumo)

def calcular_custo_total(veiculos, distancia, preco_combustivel):
    custo_total = sum(veiculo.calcular_custo(distancia, preco_combustivel) for veiculo in veiculos)
    return custo_total

# Exemplo de uso
veiculos = [
    Carro("Sedan", 12),  # 12 km por litro
    Moto("Sport", 20),   # 20 km por litro
    Caminhao("Caminhão de carga", 5)  # 5 km por litro
]

preco_combustivel = 6.50  # Preço por litro em reais
distancia_viagem = 200  # Distância da viagem em km

custo_total = calcular_custo_total(veiculos, distancia_viagem, preco_combustivel)
print(f"Custo total da viagem: R$ {custo_total:.2f}")
