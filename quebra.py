import pygame
import sys

# Inicialização do Pygame
pygame.init()

# ================= Configurações da Tela =================
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Quebra Bloco - Completo")

# ================= Cores =================
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 50, 50)
VERDE = (50, 255, 50)  # Cor dos blocos especiais
AZUL = (50, 150, 255)
AMARELO = (255, 200, 50)

relogio = pygame.time.Clock()
FPS = 60

# ================= Variáveis do Jogador e da Bola =================
raquete_largura = 120
raquete_altura = 15
raquete_velocidade = 8
bola_raio = 10

def iniciar_bolas():
    """Retorna uma lista com a bola inicial no centro da tela."""
    return [{'x': LARGURA // 2, 'y': ALTURA // 2, 'dx': 5, 'dy': -5}]

def resetar_raquete():
    """Retorna a posição X e Y inicial da raquete."""
    return LARGURA // 2 - raquete_largura // 2, ALTURA - 40

raquete_x, raquete_y = resetar_raquete()
bolas = iniciar_bolas()

# ================= Sistema de Mapas =================
bloco_largura = 45
bloco_altura = 15
espaco = 5
margem_x = 25
margem_y = 40

# Mapas desenhados com: 
# 0 = Vazio, 1 = Bloco Normal, 2 = Bloco Especial (Multiplica Bola)
MAPAS = [
    [   # NÍVEL 1: Introdução ao bloco especial
        "111111111111111",
        "111111111111111",
        "111111211111111",
        "111111111111111",
        "111111111111111"
    ],
    [   # NÍVEL 2: Padrão xadrez com especiais nas pontas
        "201010101010102",
        "010101010101010",
        "101010101010101",
        "010101010101010",
        "101010101010101",
        "010101010101010"
    ],
    [   # NÍVEL 3: Pirâmide
        "000000020000000",
        "000000111000000",
        "000001121100000",
        "000011111110000",
        "000111111111000",
        "001211111112100",
        "011111111111110",
        "111111111111111"
    ],
    [   # NÍVEL 4: Desafio final antigo
        "111111211111111",
        "111111111111111",
        "110000000000011",
        "110000202000011",
        "110001111100011",
        "110001111100011",
        "110000000000011",
        "210000000000012",
        "111111111111111"
    ],
    [   # NÍVEL 5: Letra "X"
        "100000000000001",
        "010000000000010",
        "001000020000100",
        "000100000001000",
        "000011111110000",
        "000100000001000",
        "001000020000100",
        "010000000000010",
        "100000000000001"
    ],
    [   # NÍVEL 6: Invasor do Espaço (Space Invader)
        "000010000010000",
        "000001000100000",
        "000011111110000",
        "000110111011000",
        "001111111111100",
        "001011111110100",
        "001010000010100",
        "000001101100000",
        "000000020000000"
    ]
]

def carregar_nivel(indice_nivel):
    """Lê o desenho do mapa e gera os blocos correspondentes com seus tipos."""
    blocos_gerados = []
    mapa_atual = MAPAS[indice_nivel]
    for linha_idx, linha in enumerate(mapa_atual):
        for col_idx, valor in enumerate(linha):
            if valor != '0':
                b_x = margem_x + col_idx * (bloco_largura + espaco)
                b_y = margem_y + linha_idx * (bloco_altura + espaco)
                rect_bloco = pygame.Rect(b_x, b_y, bloco_largura, bloco_altura)
                blocos_gerados.append({'rect': rect_bloco, 'tipo': valor})
    return blocos_gerados

nivel_atual = 0
blocos = carregar_nivel(nivel_atual)

# Estados do jogo: "JOGANDO", "GAME_OVER", "VENCEU"
estado_jogo = "JOGANDO"

# ================= Loop Principal do Jogo =================
rodando = True
while rodando:
    # 1. Checar eventos (como fechar a janela ou reiniciar)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        # Se o jogador apertar uma tecla
        if evento.type == pygame.KEYDOWN:
            # Se o jogo acabou e ele apertar 'R', reinicia tudo
            if estado_jogo in ["GAME_OVER", "VENCEU"] and evento.key == pygame.K_r:
                nivel_atual = 0
                blocos = carregar_nivel(nivel_atual)
                raquete_x, raquete_y = resetar_raquete()
                bolas = iniciar_bolas()
                estado_jogo = "JOGANDO"

    if estado_jogo == "JOGANDO":
        # 2. Movimentação da Raquete
        teclas = pygame.key.get_pressed()
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and raquete_x > 0:
            raquete_x -= raquete_velocidade
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and raquete_x < LARGURA - raquete_largura:
            raquete_x += raquete_velocidade

        raquete = pygame.Rect(raquete_x, raquete_y, raquete_largura, raquete_altura)

        # 3. Movimentação e Colisão das Bolas
        for bola in bolas[:]: 
            bola['x'] += bola['dx']
            bola['y'] += bola['dy']

            # Colisão com paredes laterais
            if bola['x'] - bola_raio <= 0 or bola['x'] + bola_raio >= LARGURA:
                bola['dx'] *= -1 
            
            # Colisão com o teto
            if bola['y'] - bola_raio <= 0:
                bola['dy'] *= -1 
            
            # Se a bola cair no fundo da tela, ela some
            if bola['y'] >= ALTURA:
                bolas.remove(bola)
                continue 

            bola_rect = pygame.Rect(bola['x'] - bola_raio, bola['y'] - bola_raio, bola_raio * 2, bola_raio * 2)

            # Colisão com a Raquete
            if bola_rect.colliderect(raquete) and bola['dy'] > 0:
                bola['dy'] *= -1
                diferenca_centro = (bola['x'] - (raquete_x + raquete_largura / 2)) / (raquete_largura / 2)
                bola['dx'] = diferenca_centro * 6

            # Colisão com os Blocos
            bloco_colidido = None
            for bloco in blocos:
                if bola_rect.colliderect(bloco['rect']):
                    bola['dy'] *= -1 
                    bloco_colidido = bloco
                    break 

            if bloco_colidido:
                # Se for o bloco verde, multiplica a bola
                if bloco_colidido['tipo'] == '2':
                    nova_bola = {
                        'x': bola['x'], 
                        'y': bola['y'], 
                        'dx': -bola['dx'], 
                        'dy': bola['dy']
                    }
                    bolas.append(nova_bola)
                
                # Remove o bloco destruído
                blocos.remove(bloco_colidido)

        # 4. Condições de Vitória ou Game Over
        if len(bolas) == 0:
            estado_jogo = "GAME_OVER"

        elif len(blocos) == 0:
            nivel_atual += 1
            if nivel_atual < len(MAPAS):
                blocos = carregar_nivel(nivel_atual)
                raquete_x, raquete_y = resetar_raquete()
                bolas = iniciar_bolas()
                pygame.time.delay(500)
            else:
                estado_jogo = "VENCEU"

    # 5. Desenhar os elementos na tela
    TELA.fill(PRETO) 

    if estado_jogo == "VENCEU":
        fonte = pygame.font.SysFont(None, 70)
        texto = fonte.render("PARABÉNS, VOCÊ ZEROU!", True, AMARELO)
        TELA.blit(texto, (LARGURA // 2 - 290, ALTURA // 2 - 50))
        
        fonte_sub = pygame.font.SysFont(None, 30)
        texto_sub = fonte_sub.render("Pressione 'R' para jogar novamente", True, BRANCO)
        TELA.blit(texto_sub, (LARGURA // 2 - 170, ALTURA // 2 + 20))
        
    elif estado_jogo == "GAME_OVER":
        fonte = pygame.font.SysFont(None, 70)
        texto = fonte.render("GAME OVER", True, VERMELHO)
        TELA.blit(texto, (LARGURA // 2 - 150, ALTURA // 2 - 50))
        
        fonte_sub = pygame.font.SysFont(None, 30)
        texto_sub = fonte_sub.render("Pressione 'R' para recomeçar", True, BRANCO)
        TELA.blit(texto_sub, (LARGURA // 2 - 140, ALTURA // 2 + 20))

    else:
        # Mostra o nível no topo
        fonte_nivel = pygame.font.SysFont(None, 30)
        texto_nivel = fonte_nivel.render(f"Nível: {nivel_atual + 1}", True, BRANCO)
        TELA.blit(texto_nivel, (10, 10))

        # Desenha raquete
        pygame.draw.rect(TELA, AZUL, raquete)
        
        # Desenha as bolas
        for bola in bolas:
            pygame.draw.circle(TELA, BRANCO, (int(bola['x']), int(bola['y'])), bola_raio)
        
        # Desenha os blocos com base no tipo
        for bloco in blocos:
            if bloco['tipo'] == '1':
                cor_bloco = VERMELHO
            elif bloco['tipo'] == '2':
                cor_bloco = VERDE
            pygame.draw.rect(TELA, cor_bloco, bloco['rect'])

    pygame.display.flip()
    relogio.tick(FPS)

pygame.quit()
sys.exit()