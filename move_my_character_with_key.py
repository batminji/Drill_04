from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

keroro_stand = load_image('keroro_stand.png')
keroro_right = load_image('keroro_right.png')
keroro_left = load_image('keroro_left.png')
keroro_up = load_image('keroro_up.png')
keroro_down = load_image('keroro_down.png')

keroro_right_down = load_image('keroro_right_down.png')
keroro_left_down = load_image('keroro_left_down.png')
keroro_right_up = load_image('keroro_right_up.png')
keroro_left_up = load_image('keroro_left_up.png')

def motion():
    global running, dir_x, dir_y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            if event.key == SDLK_LEFT:
                dir_x -= 1
            if event.key == SDLK_UP:
                dir_y += 1
            if event.key == SDLK_DOWN:
                dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            if event.key == SDLK_LEFT:
                dir_x += 1
            if event.key == SDLK_UP:
                dir_y -= 1
            if event.key == SDLK_DOWN:
                dir_y += 1

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if dir_x == 0 and dir_y == 0: # stand
        keroro_stand.clip_draw(0, 0, 265, 390, x, y, 130, 195)
    elif dir_x > 0 and dir_y == 0 : # right
        keroro_right.clip_draw(frame * 250, 0, 250, 345, x, y, 130, 195)
    elif dir_x < 0 and dir_y == 0 : # left
        keroro_left.clip_draw(frame * 250, 0, 250, 345, x, y, 130, 195)
    elif dir_x == 0 and dir_y > 0 : # up
        keroro_up.clip_draw(frame * 300, 0, 300, 355, x, y, 150, 195)
    elif dir_x == 0 and dir_y < 0 : # down
        keroro_down.clip_draw(frame * 300, 0, 300, 355, x, y, 150, 185)
    elif dir_x < 0 and dir_y > 0 : # left_up
        keroro_left_up.clip_draw(frame * 290, 0, 290, 345, x, y, 130, 185)
    elif dir_x > 0 and dir_y > 0 : # right_up
        keroro_right_up.clip_draw(frame * 290, 0, 290, 345, x, y, 130, 195)
    elif dir_x < 0 and dir_y < 0 : # left_down
        keroro_left_down.clip_draw(frame * 260, 0, 260, 350, x, y, 130, 195)
    elif dir_x > 0 and dir_y < 0 : # right_down
        keroro_right_down.clip_draw(frame * 260, 0, 260, 350, x, y, 130, 195)

    update_canvas()
    motion()
    frame = (frame + 1) % 4
    x += dir_x * 10
    y += dir_y * 10
    delay(0.05)