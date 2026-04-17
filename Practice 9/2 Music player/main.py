import pygame as pg
from button import RectButton, ImageButton
from player import Player

WIDTH = 1600
HEIGHT = 900
FPS = 60

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

# buttons and labels that are secretly buttons because I'm lazy
track_number = RectButton(x=450, y=500, width=700, height=100, color="#000000", text="", text_color="#FFFFFF", text_size=36)
track_name = RectButton(x=450, y=100, width=700, height=100, color="#000000", text="", text_color="#FFFFFF", text_size=36)
track_duration = RectButton(x=450, y=200, width=700, height=100, color="#000000", text="", text_color="#FFFFFF", text_size=36)
btn_skip_back = ImageButton(x=450, y=400, width=100, height=100, img_path="images/skip_back.png")
btn_back = ImageButton(x=600, y=400, width=100, height=100, img_path="images/back.png")
btn_play = ImageButton(x=750, y=400, width=100, height=100, img_path="images/play.png")
btn_forward = ImageButton(x=900, y=400, width=100, height=100, img_path="images/forward.png")
btn_skip_forward = ImageButton(x=1050, y=400, width=100, height=100, img_path="images/skip_forward.png")
btns = [btn_skip_back, btn_back, btn_play, btn_forward, btn_skip_forward, track_name, track_duration, track_number]

# music player
player = Player()
player.load_playlist("music")

running = True
while running:
    # delta time
    delta = clock.tick(FPS)
    player.update(delta)

    # event handling
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE or e.key == pg.K_q: # Quit
                running = False
            if e.key == pg.K_p: # Play
                if not player.is_playing:
                    btn_play.update_image("images/pause.png")
                    player.resume()
            if e.key == pg.K_s: # Stop
                if player.is_playing:
                    btn_play.update_image("images/play.png")
                    player.pause()
            if e.key == pg.K_n: # Next track
                player.skip_forward()
            if e.key == pg.K_b: # Previous track
                player.skip_back()

    # update buttons
    for b in btns:
        b.update()
    
    if btn_play.is_just_released():
        if player.is_playing:
            btn_play.update_image("images/play.png")
            player.pause()
        else:
            btn_play.update_image("images/pause.png")
            player.resume()

    if btn_skip_back.is_just_released():
        player.skip_back()

    if btn_back.is_just_released():
        player.back()

    if btn_skip_forward.is_just_released():
        player.skip_forward()

    if btn_forward.is_just_released():
        player.forward()

    # update track info
    track_name.update_text(str(player.current_track_name), "#FFFFFF")
    sec = int(player.playback_seconds)
    dur = int(player.current_track_duration)
    formatted_duration = f"{sec // 60}:{sec % 60 // 10}{sec % 60 % 10} / {dur // 60}:{dur % 60 // 10}{dur % 60 % 10}"
    track_duration.update_text(formatted_duration, "#FFFFFF")
    track_number.update_text(f"{player.current_track}/{len(player.tracks)}", "#FFFFFF")

    # background
    sc.fill("#000000")
    
    # draw buttons
    for b in btns:
        b.draw(sc)

    # screen update
    pg.display.flip()

# quit procedures
player.quit()
pg.quit()

