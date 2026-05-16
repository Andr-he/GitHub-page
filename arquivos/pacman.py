import pygame
import sys
import math
import random

pygame.init()

# ── Configurações ──────────────────────────────────────────────
CELL       = 28
COLS       = 20
ROWS       = 22
W          = COLS * CELL
H          = ROWS * CELL + 60
FPS        = 60
FRIGHT_DUR = 300

BLACK  = (0,   0,   0)
BLUE   = (33,  33, 222)
YELLOW = (255, 255,   0)
WHITE  = (255, 255, 255)
ORANGE = (255, 165,   0)
RED    = (220,   0,   0)
PINK   = (255, 182, 193)
CYAN   = (  0, 255, 255)
DBLUE  = ( 20,  20, 180)
LBLUE  = (150, 150, 255)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pac-Man")
clock  = pygame.time.Clock()
font_s = pygame.font.SysFont("monospace", 18, bold=True)

MAP = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
    [1,2,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,2,1],
    [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1],
    [1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,0,1,1,3,3,3,3,3,3,1,1,0,1,1,1,1],
    [1,1,1,1,0,1,1,3,3,3,3,3,3,1,1,0,1,1,1,1],
    [9,9,9,9,0,1,1,3,3,3,3,3,3,1,1,0,9,9,9,9],
    [1,1,1,1,0,1,1,3,3,3,3,3,3,1,1,0,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1],
    [1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1],
    [1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
    [1,2,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,2,1],
    [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

ROWS_MAP = len(MAP)
COLS_MAP = len(MAP[0])

def cell_val(r, c):
    if r < 0 or r >= ROWS_MAP or c < 0 or c >= COLS_MAP:
        return 1
    return MAP[r][c]

def is_wall(r, c):
    return cell_val(r, c) == 1

def is_ghost_house(r, c):
    return cell_val(r, c) == 3

def build_dots():
    dots, powers = {}, {}
    for r, row in enumerate(MAP):
        for c, v in enumerate(row):
            if v == 0:
                dots[(r, c)] = True
            elif v == 2:
                powers[(r, c)] = True
    return dots, powers

# ── Pac-Man ──────────────────────────────────────────────────
class Pacman:
    SPEED = 0.10

    def __init__(self):
        self.reset()

    def reset(self):
        self.x      = 9.5
        self.y      = 16.0
        self.dx     = 0
        self.dy     = 0
        self.ndx    = 0
        self.ndy    = 0
        self.mouth  = 0.0
        self.mdir   = 1
        self.facing = 0
        self.dead   = False
        self.dtimer = 0

    def set_dir(self, dx, dy):
        self.ndx, self.ndy = dx, dy

    def _tile_free(self, tx, ty):
        margin = 0.4
        for dr in [-margin, margin]:
            for dc in [-margin, margin]:
                r = int(math.floor(ty + dr))
                c = int(math.floor(tx + dc))
                if is_wall(r, c):
                    return False
        return True

    def update(self, dots, powers):
        if self.dead:
            self.dtimer += 1
            return None

        # Tenta virar para a nova direção desejada
        nx = self.x + self.ndx * self.SPEED
        ny = self.y + self.ndy * self.SPEED
        if (self.ndx != 0 or self.ndy != 0) and self._tile_free(nx, ny):
            self.dx, self.dy = self.ndx, self.ndy

        # Move na direção atual
        nx = self.x + self.dx * self.SPEED
        ny = self.y + self.dy * self.SPEED
        if self._tile_free(nx, ny):
            self.x, self.y = nx, ny

        # Túnel lateral
        if self.x < 0:          self.x = COLS_MAP - 0.5
        if self.x >= COLS_MAP:  self.x = 0.5

        # Boca
        self.mouth += 0.06 * self.mdir
        if self.mouth >= 0.40: self.mdir = -1
        if self.mouth <= 0.02: self.mdir =  1

        # Direção visual
        if   self.dx ==  1: self.facing =   0
        elif self.dx == -1: self.facing = 180
        elif self.dy == -1: self.facing = 270
        elif self.dy ==  1: self.facing =  90

        # Comer pontos
        pr, pc = round(self.y), round(self.x)
        if (pr, pc) in dots:
            del dots[(pr, pc)]
            return "dot"
        if (pr, pc) in powers:
            del powers[(pr, pc)]
            return "power"
        return None

    def draw(self, surf):
        cx = int(self.x * CELL + CELL // 2)
        cy = int(self.y * CELL + CELL // 2) + 30
        r  = CELL // 2 - 2

        if self.dead:
            pct = min(self.dtimer / 40, 1.0)
            if pct < 1.0:
                gap = pct * math.pi
                f   = math.radians(self.facing)
                pts = [(cx, cy),
                       (cx + int(r * math.cos(f + gap)), cy - int(r * math.sin(f + gap))),
                       (cx + int(r * math.cos(f - gap)), cy - int(r * math.sin(f - gap)))]
                pygame.draw.polygon(surf, YELLOW, pts)
            return

        gap     = self.mouth * math.pi
        f       = math.radians(self.facing)
        start_a = f + gap
        end_a   = f - gap + math.pi * 2
        pygame.draw.arc(surf, YELLOW, (cx - r, cy - r, 2*r, 2*r),
                        min(start_a, end_a), max(start_a, end_a), r)
        p1 = (cx + int(r * math.cos(start_a)), cy - int(r * math.sin(start_a)))
        p2 = (cx + int(r * math.cos(end_a)),   cy - int(r * math.sin(end_a)))
        pygame.draw.line(surf, YELLOW, (cx, cy), p1, 2)
        pygame.draw.line(surf, YELLOW, (cx, cy), p2, 2)


# ── Fantasma ─────────────────────────────────────────────────
class Ghost:
    SPEED      = 0.08
    FRIGHT_SPD = 0.05

    def __init__(self, name, start_r, start_c, color, release_delay):
        self.name          = name
        self.color         = color
        self.home_r        = start_r
        self.home_c        = start_c
        self.release_delay = release_delay
        self.reset()

    def reset(self):
        self.x             = float(self.home_c)
        self.y             = float(self.home_r)
        self.dx            = 0
        self.dy            = 0
        self.fright        = False
        self.eaten         = False
        self.release_timer = 0
        self.released      = (self.release_delay == 0)

    def _at_center(self):
        return abs(self.x - round(self.x)) < 0.18 and \
               abs(self.y - round(self.y)) < 0.18

    def _choose_dir(self, pac):
        r = round(self.y)
        c = round(self.x)
        dirs_all = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        opp = (-self.dy, -self.dx)

        def passable(dr, dc):
            nr, nc = r + dr, c + dc
            v = cell_val(nr, nc)
            if v == 1: return False
            if self.released and not self.eaten and v == 3: return False
            return True

        candidates = [d for d in dirs_all if d != opp and passable(*d)]
        if not candidates:
            candidates = [d for d in dirs_all if passable(*d)]
        if not candidates:
            return self.dx, self.dy

        if self.eaten:
            target_r, target_c = self.home_r, self.home_c
        elif self.fright:
            return random.choice(candidates)
        else:
            target_r, target_c = round(pac.y), round(pac.x)

        def dist(d):
            nr, nc = r + d[0], c + d[1]
            return (nr - target_r) ** 2 + (nc - target_c) ** 2

        return min(candidates, key=dist)

    def update(self, pac):
        self.release_timer += 1
        if not self.released and self.release_timer >= self.release_delay:
            self.released = True
            self.dy = -1
            self.dx = 0

        spd = self.FRIGHT_SPD if (self.fright and not self.eaten) else self.SPEED
        if self.eaten:
            spd = self.SPEED * 2.0

        if self._at_center():
            self.dx, self.dy = self._choose_dir(pac)

        nx = self.x + self.dx * spd
        ny = self.y + self.dy * spd

        if nx < 0:         nx = COLS_MAP - 0.5
        if nx >= COLS_MAP: nx = 0.5

        nr = round(ny)
        nc = round(nx)
        v  = cell_val(nr, nc)
        blocked = (v == 1) or (self.released and not self.eaten and v == 3)
        if not blocked:
            self.x, self.y = nx, ny
        else:
            self.x = round(self.x)
            self.y = round(self.y)
            self.dx, self.dy = 0, 0

        if self.eaten:
            if abs(self.x - self.home_c) < 0.3 and abs(self.y - self.home_r) < 0.3:
                self.eaten  = False
                self.fright = False
                self.dx     = 0
                self.dy     = -1

    def draw(self, surf, fright_timer):
        cx = int(self.x * CELL + CELL // 2)
        cy = int(self.y * CELL + CELL // 2) + 30
        r  = CELL // 2 - 2

        if self.eaten:
            for ex, ey in [(-5, -4), (5, -4)]:
                pygame.draw.circle(surf, WHITE, (cx + ex, cy + ey), 4)
                pygame.draw.circle(surf, BLUE,  (cx + ex, cy + ey), 2)
            return

        if self.fright:
            blink = fright_timer < 100 and (fright_timer // 12) % 2 == 0
            color = LBLUE if blink else DBLUE
        else:
            color = self.color

        pygame.draw.ellipse(surf, color, (cx - r, cy - r, 2*r, 2*r))
        pygame.draw.rect(surf, color, (cx - r, cy, 2*r, r))
        wave_r = max(r // 4, 3)
        for i in range(4):
            wx = cx - r + wave_r + i * (wave_r * 2)
            pygame.draw.circle(surf, BLACK, (wx, cy + r), wave_r)

        eye_color   = WHITE
        pupil_color = WHITE if self.fright else BLUE
        for ex, ey in [(-5, -4), (5, -4)]:
            pygame.draw.circle(surf, eye_color,   (cx + ex, cy + ey), 4)
            pygame.draw.circle(surf, pupil_color, (cx + ex, cy + ey), 2)


# ── Desenhar mapa ─────────────────────────────────────────────
def draw_map(surf, dots, powers, frame):
    for r, row in enumerate(MAP):
        for c, v in enumerate(row):
            rx = c * CELL
            ry = r * CELL + 30
            if v == 1:
                pygame.draw.rect(surf, BLUE, (rx + 2, ry + 2, CELL - 4, CELL - 4),
                                 border_radius=4)
            if (r, c) in dots:
                pygame.draw.circle(surf, WHITE, (rx + CELL//2, ry + CELL//2), 3)
            elif (r, c) in powers:
                pulse = int(abs(math.sin(frame * 0.07)) * 3 + 5)
                pygame.draw.circle(surf, YELLOW, (rx + CELL//2, ry + CELL//2), pulse)

def draw_hud(surf, score, lives, level):
    pygame.draw.rect(surf, BLACK, (0, 0, W, 30))
    pygame.draw.rect(surf, BLACK, (0, H - 30, W, 30))
    s = font_s.render(f"PONTOS: {score}   NIVEL: {level}", True, WHITE)
    surf.blit(s, (8, 6))
    for i in range(lives):
        cx, cy = W - 28 - i * 26, 15
        pygame.draw.arc(surf, YELLOW, (cx - 10, cy - 10, 20, 20),
                        0.4, math.pi * 2 - 0.4, 10)

def draw_message(surf, lines):
    overlay = pygame.Surface((W, H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 170))
    surf.blit(overlay, (0, 0))
    for i, (txt, color, sz) in enumerate(lines):
        f = pygame.font.SysFont("monospace", sz, bold=True)
        s = f.render(txt, True, color)
        surf.blit(s, (W // 2 - s.get_width() // 2, H // 2 - 70 + i * 52))


# ── Loop principal ────────────────────────────────────────────
def main():
    dots, powers = build_dots()

    pac = Pacman()
    ghosts = [
        Ghost("blinky", 10,  9, RED,     0),
        Ghost("pinky",  10, 10, PINK,   80),
        Ghost("inky",   11,  9, CYAN,  160),
        Ghost("clyde",  11, 10, ORANGE, 240),
    ]

    score       = 0
    lives       = 3
    level       = 1
    fright      = 0
    ghost_score = 200
    frame       = 0
    state       = "start"

    while True:
        clock.tick(FPS)
        frame += 1

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if ev.type == pygame.KEYDOWN:
                if state == "start":
                    state = "play"

                elif state in ("gameover", "win"):
                    if ev.key == pygame.K_r:
                        dots, powers = build_dots()
                        pac = Pacman()
                        for g in ghosts: g.reset()
                        score = 0; lives = 3; level = 1
                        fright = 0; frame = 0
                        state = "play"

                elif state == "play":
                    if   ev.key in (pygame.K_RIGHT, pygame.K_d): pac.set_dir( 1,  0)
                    elif ev.key in (pygame.K_LEFT,  pygame.K_a): pac.set_dir(-1,  0)
                    elif ev.key in (pygame.K_UP,    pygame.K_w): pac.set_dir( 0, -1)
                    elif ev.key in (pygame.K_DOWN,  pygame.K_s): pac.set_dir( 0,  1)
                    elif ev.key == pygame.K_p:                    state = "paused"

                elif state == "paused":
                    if ev.key == pygame.K_p:
                        state = "play"

        screen.fill(BLACK)
        draw_map(screen, dots, powers, frame)

        if state == "play":
            eaten = pac.update(dots, powers)

            if eaten == "dot":
                score += 10
            elif eaten == "power":
                score += 50
                fright = FRIGHT_DUR
                ghost_score = 200
                for g in ghosts:
                    if not g.eaten:
                        g.fright = True

            if fright > 0:
                fright -= 1
                if fright == 0:
                    for g in ghosts:
                        g.fright = False

            for g in ghosts:
                g.update(pac)
                if abs(pac.x - g.x) < 0.6 and abs(pac.y - g.y) < 0.6:
                    if g.fright and not g.eaten:
                        g.eaten     = True
                        g.fright    = False
                        score      += ghost_score
                        ghost_score *= 2
                    elif not g.eaten and not pac.dead:
                        pac.dead = True

            if pac.dead and pac.dtimer >= 40:
                lives -= 1
                if lives <= 0:
                    state = "gameover"
                else:
                    pac = Pacman()
                    for g in ghosts: g.reset()
                    fright = 0

            if not dots and not powers:
                level += 1
                dots, powers = build_dots()
                pac = Pacman()
                for g in ghosts: g.reset()
                fright = 0

        for g in ghosts:
            g.draw(screen, fright)
        pac.draw(screen)
        draw_hud(screen, score, lives, level)

        if state == "start":
            draw_message(screen, [
                ("PAC-MAN", YELLOW, 48),
                ("Pressione qualquer tecla", WHITE, 22),
                ("Setas ou WASD para mover", WHITE, 18),
                ("P = pausar", WHITE, 16),
            ])
        elif state == "paused":
            draw_message(screen, [("PAUSADO  (P)", YELLOW, 36)])
        elif state == "gameover":
            draw_message(screen, [
                ("GAME OVER", RED, 46),
                (f"Pontuacao: {score}", WHITE, 28),
                ("R para reiniciar", ORANGE, 22),
            ])
        elif state == "win":
            draw_message(screen, [
                ("VOCE VENCEU!", YELLOW, 44),
                (f"Pontuacao: {score}", WHITE, 28),
                ("R para jogar de novo", ORANGE, 22),
            ])

        pygame.display.flip()

if __name__ == "__main__":
    main()
