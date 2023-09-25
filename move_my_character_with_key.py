from pico2d import *
import pyautogui

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
    if pyautogui.keyDown('right'):
        dir_x += 1
    if pyautogui.keyDown('left'):
        dir_x -= 1
    if pyautogui.keyDown('up'):
        dir_y += 1
    if pyautogui.keyDown('down'):
        dir_y -= 1

    if pyautogui.keyUp('right'):
        dir_x -= 1
    if pyautogui.keyUp('left'):
        dir_x += 1
    if pyautogui.keyUp('up'):
        dir_y -= 1
    if pyautogui.keyUp('down'):
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
        pass
    elif dir_x > 0 and dir_y == 0 : # right
        pass
    elif dir_x < 0 and dir_y == 0 : # left
        pass
    elif dir_x == 0 and dir_y > 0 : # up
        pass
    elif dir_x == 0 and dir_y < 0 : # down
        pass
    elif dir_x < 0 and dir_y > 0 : # left_up
        pass
    elif dir_x > 0 and dir_y > 0 : # right_up
        pass
    elif dir_x < 0 and dir_y < 0 : # left_down
        pass
    elif dir_x > 0 and dir_y < 0 : # right_down
        pass


    update_canvas()
    motion()
    frame = (frame + 1) % 4
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)