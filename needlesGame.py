import pgzrun  
TITLE = 'Python Needles Game  --- by Jing Tong'

# Initialize the needle image and the position
startNeedle = Actor('needle', anchor=(170+50, 1))
startNeedle.x = 200     
startNeedle.y = 300     
needles = []  

rotateSpeed = 1  
score = 0     

def draw():   
    screen.fill('white')  
    startNeedle.draw()    
    for needle in needles:  
        needle.draw()        
    screen.draw.filled_circle((400, 300), 80, 'red')  
    screen.draw.text(str(score), (50, 250),
                     fontsize=50, color='green')  
    if rotateSpeed == 0:  
        screen.draw.text("Game Over!", (10, 320), fontsize=35, color='red')

def update():   
    for needle in needles:  
        needle.angle = needle.angle + rotateSpeed  

def on_key_down():  
    global rotateSpeed, score
    if rotateSpeed >0: 
        music.play_once('spring')

    newNeedle = Actor('needle', anchor=(170+50, 1))
    newNeedle.x = 400     
    newNeedle.y = 300     

    for needle in needles:
        if newNeedle.colliderect(needle): 
            print('Game Over')
            rotateSpeed = 0  
            music.play_once('leaving')

    if rotateSpeed > 0:  
        score = score + 1  

    needles.append(newNeedle)  

pgzrun.go()   
