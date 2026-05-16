import pygame
import sys
import random

pygame.init()

# ── Resolução ──────────────────────────────────────────────────
CELL      = 24
COLS      = 30
ROWS      = 25
W         = COLS * CELL
H         = ROWS * CELL + 50
FPS_BASE  = 7       # velocidade inicial (mais lenta)
FPS_MAX   = 18      # velocidade máxima

BLACK  = (0,   0,   0)
GREEN  = (0,  200,  50)
DGREEN = (0,  140,  30)
RED    = (220,  40,  40)
WHITE  = (255, 255, 255)
YELLOW = (255, 220,   0)
ORANGE = (255, 140,   0)

# ── Tela (janela normal por padrão) ───────────────────────────
fullscreen  = False
scale       = 1.0   # escala atual (1x, 1.5x, 2x)
SCALE_STEPS = [1.0, 1.5, 2.0]
scale_idx   = 0

def make_screen():
    global screen, fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        sw = int(W * scale)
        sh = int(H * scale)
        screen = pygame.display.set_mode((sw, sh), pygame.RESIZABLE)

# Surface lógica (sempre W x H) — depois escalamos para a tela
logic = pygame.Surface((W, H))

make_screen()
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

font_l = pygame.font.SysFont("monospace", 36, bold=True)
font_m = pygame.font.SysFont("monospace", 22, bold=True)
font_s = pygame.font.SysFont("monospace", 16, bold=True)

# ── Jogo ───────────────────────────────────────────────────────
def new_game():
    cx, cy = COLS // 2, ROWS // 2
    snake  = [(cx, cy), (cx-1, cy), (cx-2, cy)]
    food   = spawn_food(snake)
    return snake, 1, 0, food, 0, 1

def spawn_food(snake):
    while True:
        pos = (random.randint(0, COLS-1), random.randint(0, ROWS-1))
        if pos not in snake:
            return pos

def draw_grid(surf):
    for r in range(ROWS):
        for c in range(COLS):
            color = (15, 15, 15) if (r + c) % 2 == 0 else (20, 20, 20)
            pygame.draw.rect(surf, color, (c*CELL, r*CELL + 50, CELL, CELL))

def draw_snake(surf, snake):
    for i, (cx, cy) in enumerate(snake):
        x, y = cx * CELL, cy * CELL + 50
        if i == 0:
            pygame.draw.rect(surf, GREEN, (x+1, y+1, CELL-2, CELL-2), border_radius=6)
            if len(snake) > 1:
                bx, by = snake[1]
                ddx, ddy = cx - bx, cy - by
            else:
                ddx, ddy = 1, 0
            if   ddx ==  1: ex1,ey1,ex2,ey2 = 14,4, 14,13
            elif ddx == -1: ex1,ey1,ex2,ey2 = 4, 4,  4,13
            elif ddy ==  1: ex1,ey1,ex2,ey2 = 4,14, 13,14
            else:            ex1,ey1,ex2,ey2 = 4, 4, 13, 4
            pygame.draw.circle(surf, WHITE, (x+ex1, y+ey1), 3)
            pygame.draw.circle(surf, WHITE, (x+ex2, y+ey2), 3)
            pygame.draw.circle(surf, BLACK, (x+ex1, y+ey1), 1)
            pygame.draw.circle(surf, BLACK, (x+ex2, y+ey2), 1)
        else:
            shade = max(60, 200 - i * 3)
            color = (0, shade, int(shade * 0.25))
            pygame.draw.rect(surf, color, (x+2, y+2, CELL-4, CELL-4), border_radius=4)

def draw_food(surf, food, frame):
    fx, fy = food
    x, y   = fx * CELL + CELL//2, fy * CELL + 50 + CELL//2
    pulse  = abs((frame % 30) - 15) / 15
    r      = int(6 + pulse * 3)
    pygame.draw.circle(surf, RED,    (x, y), r)
    pygame.draw.circle(surf, ORANGE, (x-2, y-2), max(r//3, 2))

def draw_hud(surf, score, level, spd_pct):
    pygame.draw.rect(surf, (10, 10, 10), (0, 0, W, 50))
    pygame.draw.line(surf, DGREEN, (0, 50), (W, 50), 2)
    s = font_m.render(f"PONTOS: {score}", True, WHITE)
    l = font_m.render(f"NIVEL: {level}", True, YELLOW)
    surf.blit(s, (10, 12))
    surf.blit(l, (W - l.get_width() - 10, 12))
    # Mini barra de velocidade
    bar_w = 80
    bar_x = W//2 - bar_w//2
    pygame.draw.rect(surf, (40,40,40), (bar_x, 18, bar_w, 10), border_radius=4)
    pygame.draw.rect(surf, GREEN, (bar_x, 18, int(bar_w * spd_pct), 10), border_radius=4)

def draw_message(surf, lines):
    overlay = pygame.Surface((W, H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    surf.blit(overlay, (0, 0))
    for i, (txt, color, sz) in enumerate(lines):
        f = pygame.font.SysFont("monospace", sz, bold=True)
        s = f.render(txt, True, color)
        surf.blit(s, (W//2 - s.get_width()//2, H//2 - 90 + i * 52))

def blit_scaled(dest, src):
    sw, sh = dest.get_size()
    lw, lh = src.get_size()
    ratio   = min(sw / lw, sh / lh)
    nw, nh  = int(lw * ratio), int(lh * ratio)
    scaled  = pygame.transform.smoothscale(src, (nw, nh))
    ox      = (sw - nw) // 2
    oy      = (sh - nh) // 2
    dest.fill((0, 0, 0))
    dest.blit(scaled, (ox, oy))

# ── Loop ───────────────────────────────────────────────────────
def main():
    global fullscreen, scale, scale_idx, screen

    snake, dx, dy, food, score, level = new_game()
    ndx, ndy = dx, dy
    state    = "start"
    frame    = 0
    speed    = FPS_BASE

    while True:
        clock.tick(speed)
        frame += 1

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if ev.type == pygame.KEYDOWN:
                # F11 ou F = fullscreen
                if ev.key in (pygame.K_F11, pygame.K_f):
                    fullscreen = not fullscreen
                    make_screen()

                # + / = aumenta resolução (apenas janela)
                elif ev.key in (pygame.K_PLUS, pygame.K_EQUALS, pygame.K_KP_PLUS):
                    if not fullscreen:
                        scale_idx = min(scale_idx + 1, len(SCALE_STEPS) - 1)
                        scale     = SCALE_STEPS[scale_idx]
                        make_screen()

                # - diminui resolução
                elif ev.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                    if not fullscreen:
                        scale_idx = max(scale_idx - 1, 0)
                        scale     = SCALE_STEPS[scale_idx]
                        make_screen()

                elif state == "start":
                    state = "play"

                elif state == "gameover":
                    if ev.key == pygame.K_r:
                        snake, dx, dy, food, score, level = new_game()
                        ndx, ndy = dx, dy
                        speed    = FPS_BASE
                        state    = "play"

                elif state == "play":
                    if ev.key in (pygame.K_UP,    pygame.K_w) and dy !=  1: ndx,ndy =  0,-1
                    if ev.key in (pygame.K_DOWN,  pygame.K_s) and dy != -1: ndx,ndy =  0, 1
                    if ev.key in (pygame.K_LEFT,  pygame.K_a) and dx !=  1: ndx,ndy = -1, 0
                    if ev.key in (pygame.K_RIGHT, pygame.K_d) and dx != -1: ndx,ndy =  1, 0
                    if ev.key == pygame.K_p: state = "paused"

                elif state == "paused":
                    if ev.key == pygame.K_p: state = "play"

            if ev.type == pygame.VIDEORESIZE and not fullscreen:
                screen = pygame.display.set_mode(ev.size, pygame.RESIZABLE)

        if state == "play":
            dx, dy = ndx, ndy
            hx, hy = snake[0]
            nx, ny = hx + dx, hy + dy

            if nx < 0 or nx >= COLS or ny < 0 or ny >= ROWS or (nx, ny) in snake:
                state = "gameover"
            else:
                snake.insert(0, (nx, ny))
                if (nx, ny) == food:
                    score += 10 * level
                    food   = spawn_food(snake)
                    if len(snake) % 5 == 0:
                        level += 1
                        speed  = min(FPS_BASE + (level - 1) * 1, FPS_MAX)
                else:
                    snake.pop()

        # ── Desenha na surface lógica ──
        logic.fill(BLACK)
        draw_grid(logic)
        draw_food(logic, food, frame)
        draw_snake(logic, snake)
        spd_pct = (speed - FPS_BASE) / max(FPS_MAX - FPS_BASE, 1)
        draw_hud(logic, score, level, spd_pct)

        if state == "start":
            draw_message(logic, [
                ("COBRINHA",              GREEN,  44),
                ("Qualquer tecla p/ iniciar", WHITE, 19),
                ("Setas / WASD = mover",   WHITE,  18),
                ("F11 / F = fullscreen",   YELLOW, 16),
                ("+  /  - = tamanho janela", YELLOW, 16),
            ])
        elif state == "paused":
            draw_message(logic, [("PAUSADO  (P)", YELLOW, 36)])
        elif state == "gameover":
            draw_message(logic, [
                ("GAME OVER",                   RED,    46),
                (f"Pontuacao: {score}  Nivel: {level}", WHITE, 22),
                ("R para reiniciar",            ORANGE, 20),
            ])

        # ── Escala para a tela real ──
        blit_scaled(screen, logic)
        pygame.display.flip()

if __name__ == "__main__":
    main()
