
import math
import random
import sys
import pygame

# ============================================================
# NEON SURVIVOR - A complete single-file Pygame CE game
# ============================================================

pygame.init()

WIDTH, HEIGHT = 1100, 700
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEON SURVIVOR | Last One Standing")
clock = pygame.time.Clock()

# Colors
BG = (7, 10, 24)
WHITE = (240, 248, 255)
CYAN = (50, 240, 255)
PINK = (255, 55, 150)
PURPLE = (160, 80, 255)
GREEN = (80, 255, 150)
RED = (255, 65, 85)
YELLOW = (255, 220, 80)
MUTED = (120, 145, 180)

FONT = pygame.font.SysFont("consolas", 20)
SMALL = pygame.font.SysFont("consolas", 15)
MEDIUM = pygame.font.SysFont("consolas", 30, bold=True)
BIG = pygame.font.SysFont("consolas", 64, bold=True)

# Pre-rendered background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(BG)

for _ in range(150):
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    r = random.choice([1, 1, 1, 2])
    color = random.choice([(25, 45, 75), (35, 55, 85), (60, 75, 110)])
    pygame.draw.circle(background, color, (x, y), r)

# Game state
MENU = "menu"
PLAYING = "playing"
PAUSED = "paused"
GAME_OVER = "game_over"

state = MENU

player = None
bullets = []
enemies = []
particles = []
pickups = []

score = 0
elapsed = 0.0
spawn_timer = 0.0
pickup_timer = 0.0
shake = 0.0
high_score = 0


def draw_text(surface, text, font, color, x, y, center=False):
    image = font.render(str(text), True, color)
    rect = image.get_rect()

    if center:
        rect.center = (int(x), int(y))
    else:
        rect.topleft = (int(x), int(y))

    surface.blit(image, rect)


def glow_circle(surface, color, position, radius):
    """Draw a soft glow followed by a crisp circle."""
    x, y = int(position[0]), int(position[1])

    for size, alpha in [(3.0, 15), (2.1, 25), (1.5, 40)]:
        r = max(1, int(radius * size))
        layer = pygame.Surface((r * 2 + 4, r * 2 + 4), pygame.SRCALPHA)
        pygame.draw.circle(
            layer, (*color, alpha),
            (r + 2, r + 2), r
        )
        surface.blit(layer, (x - r - 2, y - r - 2),
                      special_flags=pygame.BLEND_ADD)

    pygame.draw.circle(surface, color, (x, y), radius)


def make_burst(position, color, amount=14, speed=180):
    """Create particles at a position."""
    for _ in range(amount):
        angle = random.uniform(0, math.tau)
        velocity = random.uniform(speed * 0.25, speed)

        particles.append({
            "x": float(position[0]),
            "y": float(position[1]),
            "vx": math.cos(angle) * velocity,
            "vy": math.sin(angle) * velocity,
            "life": random.uniform(0.25, 0.65),
            "max_life": 0.65,
            "size": random.randint(2, 5),
            "color": color
        })


class Player:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.radius = 15
        self.speed = 290
        self.health = 100
        self.max_health = 100
        self.angle = 0
        self.shoot_timer = 0
        self.invulnerable = 0
        self.dash_cooldown = 0
        self.dash_time = 0
        self.kills = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()

        dx = int(keys[pygame.K_d] or keys[pygame.K_RIGHT]) - int(
            keys[pygame.K_a] or keys[pygame.K_LEFT]
        )
        dy = int(keys[pygame.K_s] or keys[pygame.K_DOWN]) - int(
            keys[pygame.K_w] or keys[pygame.K_UP]
        )

        length = math.hypot(dx, dy)

        if length:
            dx /= length
            dy /= length

        speed = self.speed * (2.5 if self.dash_time > 0 else 1)

        self.x += dx * speed * dt
        self.y += dy * speed * dt

        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angle = math.atan2(mouse_y - self.y, mouse_x - self.x)

        self.shoot_timer = max(0, self.shoot_timer - dt)
        self.invulnerable = max(0, self.invulnerable - dt)
        self.dash_cooldown = max(0, self.dash_cooldown - dt)
        self.dash_time = max(0, self.dash_time - dt)

        # Hold left mouse button to fire
        if pygame.mouse.get_pressed()[0] and self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = 0.13

    def shoot(self):
        dx = math.cos(self.angle)
        dy = math.sin(self.angle)

        bullets.append({
            "x": self.x + dx * 22,
            "y": self.y + dy * 22,
            "vx": dx * 720,
            "vy": dy * 720,
            "life": 1.25,
            "radius": 5
        })

        make_burst(
            (self.x + dx * 23, self.y + dy * 23),
            CYAN, 3, 80
        )

    def dash(self):
        if self.dash_cooldown > 0:
            return

        keys = pygame.key.get_pressed()

        dx = int(keys[pygame.K_d] or keys[pygame.K_RIGHT]) - int(
            keys[pygame.K_a] or keys[pygame.K_LEFT]
        )
        dy = int(keys[pygame.K_s] or keys[pygame.K_DOWN]) - int(
            keys[pygame.K_w] or keys[pygame.K_UP]
        )

        length = math.hypot(dx, dy)

        if length:
            dx /= length
            dy /= length
        else:
            dx = math.cos(self.angle)
            dy = math.sin(self.angle)

        self.x += dx * 65
        self.y += dy * 65

        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

        self.dash_time = 0.18
        self.dash_cooldown = 1.4
        self.invulnerable = max(self.invulnerable, 0.25)

        make_burst((self.x, self.y), CYAN, 18, 240)

    def draw(self, surface):
        # Blink while invulnerable
        if self.invulnerable > 0 and int(self.invulnerable * 20) % 2:
            return

        direction = pygame.Vector2(
            math.cos(self.angle), math.sin(self.angle)
        )
        side = pygame.Vector2(-direction.y, direction.x)

        tip = pygame.Vector2(self.x, self.y) + direction * 22
        rear = pygame.Vector2(self.x, self.y) - direction * 15
        left = rear + side * 13
        right = rear - side * 13

        points = [
            (int(tip.x), int(tip.y)),
            (int(left.x), int(left.y)),
            (int((self.x - direction.x * 5)),
             int((self.y - direction.y * 5))),
            (int(right.x), int(right.y))
        ]

        glow_circle(surface, CYAN, (self.x, self.y), 13)
        pygame.draw.polygon(surface, WHITE, points)
        pygame.draw.polygon(surface, CYAN, points, 2)


class Enemy:
    def __init__(self, difficulty):
        side = random.randrange(4)

        if side == 0:
            self.x, self.y = random.randrange(WIDTH), -30
        elif side == 1:
            self.x, self.y = WIDTH + 30, random.randrange(HEIGHT)
        elif side == 2:
            self.x, self.y = random.randrange(WIDTH), HEIGHT + 30
        else:
            self.x, self.y = -30, random.randrange(HEIGHT)

        self.kind = random.choices(
            ["normal", "fast", "tank"],
            weights=[70, 20, min(10, 2 + difficulty * 0.5)]
        )[0]

        if self.kind == "fast":
            self.radius = 10
            self.speed = random.uniform(145, 190) + difficulty * 2
            self.hp = 1
            self.color = YELLOW
            self.damage = 9
            self.points = 15
        elif self.kind == "tank":
            self.radius = 23
            self.speed = 55 + difficulty
            self.hp = 5
            self.color = PURPLE
            self.damage = 20
            self.points = 35
        else:
            self.radius = 15
            self.speed = random.uniform(75, 110) + difficulty * 1.5
            self.hp = 2
            self.color = PINK
            self.damage = 12
            self.points = 10

        self.max_hp = self.hp
        self.hit_flash = 0

    def update(self, dt):
        dx = player.x - self.x
        dy = player.y - self.y
        distance = max(1, math.hypot(dx, dy))

        self.x += dx / distance * self.speed * dt
        self.y += dy / distance * self.speed * dt
        self.hit_flash = max(0, self.hit_flash - dt)

    def draw(self, surface):
        color = WHITE if self.hit_flash > 0 else self.color

        glow_circle(surface, self.color, (self.x, self.y), self.radius)

        if self.kind == "tank":
            pygame.draw.circle(
                surface, color,
                (int(self.x), int(self.y)),
                self.radius, 3
            )
            pygame.draw.circle(
                surface, color,
                (int(self.x), int(self.y)),
                self.radius // 2, 2
            )
        else:
            pygame.draw.circle(
                surface, color,
                (int(self.x), int(self.y)),
                self.radius, 2
            )

        if self.hp < self.max_hp:
            width = self.radius * 2
            ratio = max(0, self.hp / self.max_hp)
            pygame.draw.rect(
                surface, (50, 25, 50),
                (self.x - self.radius, self.y - self.radius - 8,
                 width, 4)
            )
            pygame.draw.rect(
                surface, GREEN,
                (self.x - self.radius, self.y - self.radius - 8,
                 width * ratio, 4)
            )


def spawn_pickup():
    kind = random.choice(["health", "rapid"])
    pickups.append({
        "x": random.randint(35, WIDTH - 35),
        "y": random.randint(35, HEIGHT - 35),
        "kind": kind,
        "life": 10.0,
        "phase": random.random() * math.tau
    })


def reset_game():
    global player, bullets, enemies, particles, pickups
    global score, elapsed, spawn_timer, pickup_timer, shake, state

    player = Player()
    bullets = []
    enemies = []
    particles = []
    pickups = []

    score = 0
    elapsed = 0.0
    spawn_timer = 0.0
    pickup_timer = 7.0
    shake = 0.0
    state = PLAYING


def draw_bar(surface, x, y, width, height, ratio, color):
    ratio = max(0, min(1, ratio))
    pygame.draw.rect(surface, (30, 40, 60), (x, y, width, height))
    pygame.draw.rect(
        surface, color, (x, y, int(width * ratio), height)
    )
    pygame.draw.rect(
        surface, (80, 100, 130), (x, y, width, height), 1
    )


def draw_hud(surface):
    # Health
    draw_text(surface, "HULL", SMALL, WHITE, 22, 20)
    draw_bar(
        surface, 22, 43, 210, 13,
        player.health / player.max_health,
        GREEN if player.health > 35 else RED
    )
    draw_text(
        surface, f"{player.health}/{player.max_health}",
        SMALL, WHITE, 240, 40
    )

    # Dash cooldown
    draw_text(surface, "DASH [SPACE]", SMALL, CYAN, 22, 70)
    draw_bar(
        surface, 22, 91, 150, 7,
        1 - player.dash_cooldown / 1.4, CYAN
    )

    draw_text(
        surface, f"SCORE  {score:06d}",
        MEDIUM, WHITE, WIDTH - 25, 20
    )
    draw_text(
        surface, f"TIME  {int(elapsed // 60):02d}:{int(elapsed % 60):02d}",
        FONT, CYAN, WIDTH - 25, 58
    )
    draw_text(
        surface, f"ELIMINATIONS  {player.kills}",
        SMALL, MUTED, WIDTH - 25, 88
    )

    draw_text(
        surface, "WASD: MOVE   MOUSE: AIM   LMB: FIRE   SPACE: DASH   ESC: PAUSE",
        SMALL, MUTED, WIDTH / 2, HEIGHT - 20, center=True
    )


def draw_pickups(surface):
    for item in pickups:
        item["phase"] += 0.04
        pulse = 4 * math.sin(item["phase"])
        color = GREEN if item["kind"] == "health" else YELLOW

        glow_circle(
            surface, color, (item["x"], item["y"]),
            int(9 + pulse * 0.3)
        )

        symbol = "+" if item["kind"] == "health" else "R"
        draw_text(
            surface, symbol, SMALL, WHITE,
            item["x"], item["y"], center=True
        )


def draw_overlay(title, subtitle, hint=""):
    # Semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((3, 5, 18, 205))
    screen.blit(overlay, (0, 0))

    draw_text(screen, title, BIG, CYAN, WIDTH / 2, HEIGHT / 2 - 100, True)
    draw_text(
        screen, subtitle, MEDIUM, WHITE,
        WIDTH / 2, HEIGHT / 2 - 25, True
    )

    if hint:
        draw_text(
            screen, hint, FONT, MUTED,
            WIDTH / 2, HEIGHT / 2 + 45, True
        )


def update_particles(dt):
    for p in particles[:]:
        p["x"] += p["vx"] * dt
        p["y"] += p["vy"] * dt
        p["vx"] *= 0.96
        p["vy"] *= 0.96
        p["life"] -= dt

        if p["life"] <= 0:
            particles.remove(p)


def draw_particles(surface):
    for p in particles:
        ratio = max(0, p["life"] / p["max_life"])
        radius = max(1, int(p["size"] * ratio))
        pygame.draw.circle(
            surface, p["color"],
            (int(p["x"]), int(p["y"])), radius
        )


# Main loop
while True:
    dt = min(clock.tick(FPS) / 1000.0, 0.033)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state == PLAYING:
                    state = PAUSED
                elif state == PAUSED:
                    state = PLAYING
                elif state in (MENU, GAME_OVER):
                    pygame.quit()
                    sys.exit()

            if event.key == pygame.K_RETURN:
                if state in (MENU, GAME_OVER):
                    reset_game()
                elif state == PAUSED:
                    state = PLAYING

            if event.key == pygame.K_SPACE and state == PLAYING:
                player.dash()

            if event.key == pygame.K_r and state == GAME_OVER:
                reset_game()

    # Background
    screen.blit(background, (0, 0))

    if state == MENU:
        # Decorative moving energy rings
        t = pygame.time.get_ticks() / 1000
        for i in range(5):
            radius = 50 + i * 32 + int(5 * math.sin(t + i))
            pygame.draw.circle(
                screen, (15, 55 + i * 5, 85 + i * 5),
                (WIDTH // 2, HEIGHT // 2 - 30), radius, 1
            )

        draw_text(
            screen, "NEON", BIG, CYAN,
            WIDTH / 2, HEIGHT / 2 - 100, True
        )
        draw_text(
            screen, "SURVIVOR", BIG, PINK,
            WIDTH / 2, HEIGHT / 2 - 35, True
        )
        draw_text(
            screen, "THE ARENA DOES NOT FORGIVE",
            FONT, WHITE, WIDTH / 2, HEIGHT / 2 + 40, True
        )
        draw_text(
            screen, "SURVIVE. ELIMINATE. EVOLVE.",
            SMALL, MUTED, WIDTH / 2, HEIGHT / 2 + 75, True
        )
        draw_text(
            screen, "[ ENTER ]  START GAME",
            MEDIUM, GREEN, WIDTH / 2, HEIGHT / 2 + 140, True
        )
        draw_text(
            screen, "WASD move | Mouse aim | Left click shoot | SPACE dash",
            SMALL, MUTED, WIDTH / 2, HEIGHT - 40, True
        )

    elif state == PLAYING:
        elapsed += dt
        difficulty = elapsed / 15

        # Enemy spawning becomes faster over time
        spawn_timer -= dt
        spawn_interval = max(0.20, 0.85 - difficulty * 0.045)

        if spawn_timer <= 0:
            enemies.append(Enemy(difficulty))
            spawn_timer = spawn_interval

        # Spawn occasional pickups
        pickup_timer -= dt
        if pickup_timer <= 0:
            spawn_pickup()
            pickup_timer = random.uniform(9, 14)

        player.update(dt)

        # Bullets
        for bullet in bullets[:]:
            bullet["x"] += bullet["vx"] * dt
            bullet["y"] += bullet["vy"] * dt
            bullet["life"] -= dt

            if (
                bullet["life"] <= 0
                or bullet["x"] < -20
                or bullet["x"] > WIDTH + 20
                or bullet["y"] < -20
                or bullet["y"] > HEIGHT + 20
            ):
                bullets.remove(bullet)

        # Enemies
        for enemy in enemies:
            enemy.update(dt)

        # Bullet versus enemy collisions
        for bullet in bullets[:]:
            hit_enemy = None

            for enemy in enemies:
                distance = math.hypot(
                    bullet["x"] - enemy.x,
                    bullet["y"] - enemy.y
                )

                if distance < bullet["radius"] + enemy.radius:
                    hit_enemy = enemy
                    break

            if hit_enemy:
                hit_enemy.hp -= 1
                hit_enemy.hit_flash = 0.08

                make_burst(
                    (bullet["x"], bullet["y"]),
                    hit_enemy.color, 4, 100
                )

                if bullet in bullets:
                    bullets.remove(bullet)

                if hit_enemy.hp <= 0:
                    score += hit_enemy.points
                    player.kills += 1
                    make_burst(
                        (hit_enemy.x, hit_enemy.y),
                        hit_enemy.color, 20, 230
                    )
                    enemies.remove(hit_enemy)

        # Enemy versus player collisions
        for enemy in enemies[:]:
            distance = math.hypot(
                player.x - enemy.x, player.y - enemy.y
            )

            if distance < player.radius + enemy.radius:
                if player.invulnerable <= 0:
                    player.health -= enemy.damage
                    player.invulnerable = 0.65
                    shake = 0.15
                    make_burst(
                        (player.x, player.y), RED, 12, 180
                    )

                # Remove the enemy that hit the player
                make_burst(
                    (enemy.x, enemy.y), enemy.color, 8, 120
                )
                enemies.remove(enemy)

        # Pickups
        for item in pickups[:]:
            item["life"] -= dt
            distance = math.hypot(
                player.x - item["x"], player.y - item["y"]
            )

            if distance < player.radius + 15:
                if item["kind"] == "health":
                    player.health = min(
                        player.max_health, player.health + 25
                    )
                    make_burst((item["x"], item["y"]), GREEN, 18, 150)
                else:
                    player.shoot_timer = -0.3
                    player.speed = 360
                    pygame.time.set_timer(
                        pygame.event.EventType.USEREVENT, 1
                    ) if False else None
                    make_burst((item["x"], item["y"]), YELLOW, 18, 150)

                pickups.remove(item)

            elif item["life"] <= 0:
                pickups.remove(item)

        # Update particles
        update_particles(dt)
        shake = max(0, shake - dt)

        # Draw world with screen shake
        world = pygame.Surface((WIDTH, HEIGHT))
        world.blit(background, (0, 0))

        draw_pickups(world)

        for bullet in bullets:
            glow_circle(
                world, CYAN, (bullet["x"], bullet["y"]), bullet["radius"]
            )

        for enemy in enemies:
            enemy.draw(world)

        player.draw(world)
        draw_particles(world)

        if shake > 0:
            offset_x = random.randint(-5, 5)
            offset_y = random.randint(-5, 5)
        else:
            offset_x = offset_y = 0

        screen.blit(world, (offset_x, offset_y))
        draw_hud(screen)

        if player.health <= 0:
            state = GAME_OVER

    elif state == PAUSED:
        # Keep the last scene visible behind the pause overlay
        draw_overlay(
            "PAUSED",
            f"Score: {score}",
            "Press ENTER to resume | ESC to return to the menu"
        )

    elif state == GAME_OVER:
        draw_overlay(
            "GAME OVER",
            f"FINAL SCORE: {score}",
            f"Eliminations: {player.kills} | Survival: {int(elapsed)} seconds"
        )
        draw_text(
            screen, "[ ENTER / R ]  PLAY AGAIN",
            MEDIUM, GREEN, WIDTH / 2, HEIGHT / 2 + 105, True
        )
        draw_text(
            screen, "[ ESC ]  QUIT",
            FONT, MUTED, WIDTH / 2, HEIGHT / 2 + 150, True
        )

    pygame.display.flip()
