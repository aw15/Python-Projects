import game_framework
from pico2d import *
import title_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('resource/titleImage/kpu_credit.png')


def exit():
    global image
    del(image)



def update(frame_time):
    global logo_time

    if(logo_time>1.0):
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time+=0.01



def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()



def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()


def pause(): pass


def resume(): pass




