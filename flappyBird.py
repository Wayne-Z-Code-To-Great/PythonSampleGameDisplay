import pgzrun
import random
WIDTH = 350
HEIGHT = 600

background = Actor('background')
bird = Actor('bird')
bird.x = 50
bird.y = HEIGHT/2
bar_up = Actor('bar_up')
bar_up.x = 300
bar_up.y = 0
bar_down = Actor('bar_down')
bar_down.x = 300
bar_down.y = 600

def draw():
    background.draw()
    bar_up.draw()
    bar_down.draw()
    bird.draw()

def update():
    bird.y = bird.y + 2
    bar_up.x = bar_up.x - 2
    bar_down.x = bar_down.x - 2
    if bar_up.x < 0:
        bar_up.x = WIDTH
        bar_down.x = WIDTH
        bar_up.y = random.randint(-200, 200)
        bar_down.y = 600 + bar_up.y

def on_mouse_down():
    bird.y = bird.y - 100

pgzrun.go()