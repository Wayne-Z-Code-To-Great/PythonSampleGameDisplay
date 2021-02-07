import pgzrun
import random
WIDTH = 800
HEIGHT = 600
balls = [] #A list to hold all balls' information

for i in range(100): #randomly generate 100 balls
    x = random.randint(100, WIDTH-100)
    y = random.randint(100, HEIGHT-100)
    speedx = random.randint(1, 5)
    speedy = random.randint(1, 5)
    r = random.randint(5, 50)
    colorR = random.randint(10, 255)
    colorG = random.randint(10, 255)
    colorB = random.randint(10, 255)
    ball = [x, y, speedx, speedy, r, colorR, colorG, colorB]
    balls.append(ball)

def draw():
    screen.fill('white')
    for ball in balls:
        screen.draw.filled_circle((ball[0], ball[1]), ball[4], (ball[5], 
        ball[6], ball[7]))

def update():
    for ball in balls:
        ball[0] = ball[0] + ball[2]
        ball[1] = ball[1] + ball[3]
        if ball[0] > WIDTH-ball[4] or ball[0] < ball[4]:
            ball[2] = -ball[2]
        if ball[1] > HEIGHT-ball[4] or ball[1] < ball[4]:
            ball[3] = -ball[3]

pgzrun.go()

