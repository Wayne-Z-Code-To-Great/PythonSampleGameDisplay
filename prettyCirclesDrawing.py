import pgzrun
import random
WIDTH = 1200
HEIGHT = 600
R = 100
"""
The main purpose of this piece of code is to demonstrate the use of nested-for loops
and to show how random color can be generated using the random number generator. 
When you are constanly repeating a group of statements, it is very common to use for-loops
to reduce the redundancy. On the other hand, random events are always interesting.
"""
def draw():
    screen.fill('white')
    for x in range(R, WIDTH, 2*R):
        for y in range(R, HEIGHT, 2*R):
            for r in range(1, R, 10):
                screen.draw.filled_circle((x, y), R-r, \
                (random.randint(0, 255), random.randint(0, 255), \
                random.randint(0, 255)))

#Each time you click your mouse, a new picture will be generated     
def on_mouse_down():
    draw()

pgzrun.go()