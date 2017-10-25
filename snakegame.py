#Snake Game

#import modules
import pygame
import sys , time , random

#Initialize pygame and checking the Errors
init_errors =  pygame.init()

if ( init_errors[1] > 0):
    print ("Code had  {0} initialization errors ".format(init_errors[1]))
    sys.exit(-1)
else :
    print("There in no initialization errors")

#starting the game
#play Surface
win_size = (720,640)
Window = pygame.display.set_mode(win_size)
pygame.display.set_caption('Snake Game')
#time.sleep(10)

#Colors
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
brown = pygame.Color(165,42,42)

#Fps Controller
fpsController = pygame.time.Clock()

#Starting postion of Snake ,Snake initial body size
snakeStart = [100,50]
snakeInitialBody = [[100,50],[90,50],[80,50]]

#Food positions
foodPositions = [random.randrange(1,72)*10,random.randrange(1,64)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

#Game Over Function

def gameOver():
    gameFont = pygame.font.SysFont('monaco',72)
    gameOverSurface = gameFont.render('Sorry! Game Over :( ',True,red)
    gameOverRectange = gameOverSurface.get_rect()
    gameOverRectange.midtop  = (360,30)
    Window.blit(gameOverSurface,gameOverRectange)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit() #pygame exit
    sys.exit() #console exit

#Main Logic of the game
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit() #pygame exit
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN
            if event.key == pygame.K_ESCAPE :
                pygame.event.post(pygame.event.Event(QUIT))

    # validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
# Update snake position [x,y]
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
