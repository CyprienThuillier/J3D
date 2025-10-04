import pygame as pg

pg.init()

# loadings
icon = pg.image.load("assets/icon.png")
wqsd = pg.image.load("assets/wqsd.png")
wqsd = pg.transform.smoothscale(wqsd, (270, 180))

# root settings
WIDTH, HEIGHT = 1080, 720
root = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("SAE")
pg.display.set_icon(icon)

clock = pg.time.Clock()

# player settings
player_width, player_height = 25, 25
player_x, player_y = 50, 50
player_speed_x = 0
player_speed_y = 0
PLAYER_ACC = 2
PLAYER_FRICTION = 0.9
PLAYER_MAX_SPEED = 12

# world settings
GRAVITY = 0.9

# wqsd settings
wqsd_rect = wqsd.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
fade_duration = 2000
display_duration = 4000
start_time = pg.time.get_ticks()

running = True
while running:
    now = pg.time.get_ticks()
    elapsed = now - start_time

    # events gestion
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and player_y >= HEIGHT - player_height - 3:
                player_speed_y = -15

    # player moving
    keys = pg.key.get_pressed()
    if keys[pg.K_q]:
        player_speed_x -= PLAYER_ACC
    if keys[pg.K_d]:
        player_speed_x += PLAYER_ACC

    # friction
    player_speed_x *= PLAYER_FRICTION

    if player_speed_x > PLAYER_MAX_SPEED:
        player_speed_x = PLAYER_MAX_SPEED
    if player_speed_x < -PLAYER_MAX_SPEED:
        player_speed_x = -PLAYER_MAX_SPEED

    # gravity
    player_speed_y += GRAVITY

    # moves
    player_x += player_speed_x
    player_y += player_speed_y

    # colisions
    if player_x < 3:
        player_x = 3
        player_speed_x = 0
    if player_x > WIDTH - player_width - 3:
        player_x = WIDTH - player_width - 3
        player_speed_x = 0
    if player_y > HEIGHT - player_height - 3:
        player_y = HEIGHT - player_height - 3
        player_speed_y = 0
    if player_y < 0:
        player_y = 0
        player_speed_y = 0

    # root display
    root.fill((0, 0, 0))

    # game display
    pg.draw.rect(root, (255, 255, 255), (player_x, player_y, player_width, player_height), 0, 5)

    if elapsed < display_duration:
        if elapsed < fade_duration:
            alpha = int(255 * (elapsed / fade_duration))
        elif elapsed > display_duration - fade_duration:
            alpha = int(255 * ((display_duration - elapsed) / fade_duration))
        else:
            alpha = 255

        wqsd_fade = wqsd.copy()
        wqsd_fade.set_alpha(alpha)
        root.blit(wqsd_fade, wqsd_rect)

    # root update
    pg.display.flip()
    clock.tick(60)

pg.quit()
