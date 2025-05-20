def calcular_engajamento(curtidas, comentarios, compartilhamentos, seguidores, alcance, impressoes):
    engajamento_por_seguidores = (curtidas + comentarios + compartilhamentos) / seguidores * 100 if seguidores else 0
    engajamento_por_alcance = (curtidas + comentarios + compartilhamentos) / alcance * 100 if alcance else 0
    engajamento_por_impressoes = (curtidas + comentarios + compartilhamentos) / impressoes * 100 if impressoes else 0
    
    return engajamento_por_seguidores, engajamento_por_alcance, engajamento_por_impressoes

def main():
    curtidas = int(input("Digite o número de curtidas: "))
    comentarios = int(input("Digite o número de comentários: "))
    compartilhamentos = int(input("Digite o número de compartilhamentos: "))
    seguidores = int(input("Digite o número de seguidores: "))
    alcance = int(input("Digite o número de alcance: "))
    impressoes = int(input("Digite o número de impressões: "))

    engajamento_seguidores, engajamento_alcance, engajamento_impressoes = calcular_engajamento(
        curtidas, comentarios, compartilhamentos, seguidores, alcance, impressoes
    )

    print(f"\nEngajamento por seguidores: {engajamento_seguidores:.2f}%")
    print(f"Engajamento por alcance: {engajamento_alcance:.2f}%")
    print(f"Engajamento por impressões: {engajamento_impressoes:.2f}%")

if __name__ == "__main__":
    main()
