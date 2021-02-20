import pgzrun
WIDTH = 350
HEIGHT = 600

background = Actor('background')
bird = Actor('bird')
bird.x = 50
bird.y = HEIGHT/2

def draw():
    background.draw()
    bird.draw()


pgzrun.go()