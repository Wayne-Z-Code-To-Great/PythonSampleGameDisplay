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
score = 0
speed = 3

def draw():
    background.draw()
    bar_up.draw()
    bar_down.draw()
    bird.draw()
    screen.draw.text(str(score), (30, 30), 
                    fontsize=50, color='green')

def update():
    global score, speed
    bird.y = bird.y + 2
    bar_up.x = bar_up.x - speed
    bar_down.x = bar_down.x - speed
    if bar_up.x < 0:
        bar_up.x = WIDTH
        bar_down.x = WIDTH
        bar_up.y = random.randint(-200, 200)
        bar_down.y = 600 + bar_up.y
        score = score + 1
        if (score % 5 ==0):
            speed = speed + 1
    if bird.colliderect(bar_up) or bird.colliderect(bar_down) \
                or bird.y<0 or bird.y>HEIGHT:
        print('Failed')
        score = 0
        speed = 3
        bird.x = 50
        bird.y = HEIGHT/2
        bar_up.x = WIDTH
        bar_up.y = 0
        bar_down.x = WIDTH
        bar_down.y = 600

def on_mouse_down():
    bird.y = bird.y - 100

pgzrun.go()