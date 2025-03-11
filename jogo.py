import random  # Importa o módulo random, que contém funções para gerar números aleatórios.

# Gera um número aleatório entre 1 e 10 e o armazena na variável 'numero_secreto'.
numero_secreto = random.randint(1, 10)
tentativas = 0  # Inicializa a variável 'tentativas' para rastrear quantas tentativas o jogador já fez.
max_tentativas = 5  # Define o número máximo de tentativas permitidas para o jogador.

print("Bem-vindo ao jogo de adivinhação!")  # Exibe uma mensagem inicial de boas-vindas ao jogador.
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")  # Dá instruções ao jogador sobre o objetivo do jogo.

# Loop do jogo: Continua até que o jogador esgote o número máximo de tentativas ou acerte o número.
while tentativas < max_tentativas:
    # Captura a entrada do jogador e converte-a para um número inteiro.
    # A entrada do usuário é o palpite de qual número ele acha que é o 'numero_secreto'.
    palpite = int(input("Digite seu palpite: "))

    # Incrementa a contagem de tentativas a cada palpite realizado.
    tentativas += 1

    # Verifica se o palpite do jogador está correto.
    if palpite == numero_secreto:
        # Se o jogador acertar, exibe uma mensagem de sucesso e encerra o jogo.
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        # Informa ao jogador que o número secreto é maior e pede para tentar novamente.
        print("Quase lá! Tente um número maior.")
    else:
        # Informa ao jogador que o número secreto é menor e pede para tentar novamente.
        print("Quase lá! Tente um número menor.")

    # Informa ao jogador quantas tentativas restam, caso ele não tenha atingido o limite ainda.
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# Este bloco 'else' executa se o jogador usar todas as tentativas sem acertar o número.
else:
    # Exibe uma mensagem com o número secreto e informa o fim do jogo.
    print("Infelizmente, você não acertou. O número era", numero_secreto)
    print("Fim do jogo!")
