class Calculadora:
    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b

# Testando os métodos estáticos
print(Calculadora.soma(10, 5))        # Saída: 15
print(Calculadora.subtracao(10, 5))   # Saída: 5
