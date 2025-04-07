def desenhar_forca(erros):
    partes = [
        " O ",  # cabeça
        "/|\\", # corpo e braços
        " | ",  # tronco
        "/ \\"  # pernas
    ]

    forca = [
        "_____\n",
        "|   |\n",
        "|   {}\n".format(partes[0] if erros > 0 else ""),
        "|  {}{}\n".format(partes[1] if erros > 1 else "", " " if erros <= 1 else ""),
        "|  {}\n".format(partes[2] if erros > 2 else ""),
        "| {}\n".format(partes[3] if erros > 3 else "")
    ]

    print("".join(forca))


palavra_secreta = "girafa"
letras_acertadas = ["_" for _ in palavra_secreta]
tentativas = 6
erros = 0

while tentativas > 0 and "_" in letras_acertadas:
    print("\nPalavra:", " ".join(letras_acertadas))
    palpite = input("Digite uma letra: ").strip().lower()

    if not palpite.isalpha() or len(palpite) != 1:
        print("Por favor, digite apenas uma letra válida.")
        continue

    if palpite in letras_acertadas:
        print("Você já acertou essa letra!")
        continue

    if palpite in palavra_secreta:
        indices = [i for i, letra in enumerate(palavra_secreta) if letra == palpite]
        for i in indices:
            letras_acertadas[i] = palavra_secreta[i]
        print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        erros += 1
        print(f"Ops! A letra '{palpite}' não está na palavra.")
        desenhar_forca(erros)
        print(f"Você tem {tentativas} tentativa(s) restante(s).")

if "_" not in letras_acertadas:
    print("\nParabéns, você ganhou! A palavra era:", palavra_secreta.upper())
else:
    desenhar_forca(erros)
    print("\nQue pena! Você perdeu. A palavra era:", palavra_secreta.upper())
