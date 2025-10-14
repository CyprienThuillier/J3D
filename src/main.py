import pygame as pg

pg.init()

# loadings
icon = pg.image.load("assets/icon.png")
wqsd = pg.image.load("assets/wqsd.png")
wqsd = pg.transform.smoothscale(wqsd, (270, 180))
settings_btn = pg.image.load("assets/settings.png")
settings_btn = pg.transform.smoothscale(settings_btn, (50, 50))
play_btn = pg.image.load("assets/play.png")
play_btn = pg.transform.smoothscale(play_btn, (210.5, 74))
paused_txt = pg.image.load("assets/paused.png")
paused_txt = pg.transform.smoothscale(paused_txt, (350, 350))

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
playing = True
cursor_state = "arrow"  # "arrow" ou "hand"

while running:
    now = pg.time.get_ticks()
    elapsed = now - start_time

    mouse_pos = pg.mouse.get_pos()
    play_btn_rect = play_btn.get_rect(topleft=(WIDTH // 2 - 100, HEIGHT // 2 - 100))
    mouse_on_play = not playing and play_btn_rect.collidepoint(mouse_pos)
    play_clicked = False

    # events gestion
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and player_y >= HEIGHT - player_height - 3 and playing:
                player_speed_y = -15
            if event.key == pg.K_ESCAPE:
                playing = not playing
        if event.type == pg.MOUSEBUTTONDOWN and mouse_on_play:
            play_clicked = True

    if play_clicked:
        playing = True

    if playing:
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

        # collisions
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
    pg.draw.rect(root, (255, 255, 255), (player_x, player_y, player_width, player_height), 0, 5)

    if not playing:
        root.blit(paused_txt, (WIDTH // 2 - 350 // 2, HEIGHT // 2 - 350 // 2 - 200))
        root.blit(play_btn, (WIDTH // 2 - 100, HEIGHT // 2 - 100))

        # Curseur main si sur le bouton play
        if mouse_on_play:
            if cursor_state != "hand":
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                cursor_state = "hand"
        else:
            if cursor_state != "arrow":
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                cursor_state = "arrow"
    else:
        if cursor_state != "arrow":
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
            cursor_state = "arrow"
    if playing:
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

    pg.display.flip()
    clock.tick(60)

pg.quit()
