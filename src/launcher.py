import pygame as pg

pg.init()

# IMAGES
icon = pg.image.load("assets/icon.png")
title = pg.image.load("assets/title.png")
play_btn = pg.image.load("assets/play.png")
play_btn = pg.transform.smoothscale(play_btn, (210, 74))
settings_btn = pg.image.load("assets/settings.png")
settings_btn = pg.transform.smoothscale(settings_btn, (50, 50))

# ROOT 
WIDTH, HEIGHT = 800, 720
root = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("J3D")
pg.display.set_icon(icon)
cursor_state = "arrow"

# RECT 
play_btn_rect = play_btn.get_rect(topleft=(WIDTH // 2 - 100, HEIGHT // 2))
settings_btn_rect = settings_btn.get_rect(topleft=(10, 10))

# GAME
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False       

        if event.type == pg.MOUSEBUTTONDOWN:
            if hov_play:
                print("Play!")
            if hov_settings:
                print("Settings!")

    mouse_pos = pg.mouse.get_pos()
    hov_play = play_btn_rect.collidepoint(mouse_pos)
    hov_settings = settings_btn_rect.collidepoint(mouse_pos)
    hovering = play_btn_rect.collidepoint(mouse_pos) or settings_btn_rect.collidepoint(mouse_pos)

    if hovering and cursor_state != "hand":
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        cursor_state = "hand"
    elif not hovering and cursor_state != "arrow":
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        cursor_state = "arrow"

    # Rendu
    root.fill((0, 0, 0))
    root.blit(settings_btn, (10, 10))
    root.blit(title, (150, 0))
    root.blit(play_btn, (WIDTH // 2 - 100, HEIGHT // 2))

    pg.display.flip()

pg.quit()
