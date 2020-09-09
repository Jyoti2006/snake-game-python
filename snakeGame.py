# Snake Game

# imports
import pygame
import random
import time
import sys

# Initialize pygame
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors... Exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("Pygame successfully initialized")

# Surface
playSurface=pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake Game!')
time.sleep(5)

# Colors
red=pygame.Color(255,0,0)   # gameover
green=pygame.Color(0,255,0) # snake
black=pygame.Color(0,0,0)   # score
white=pygame.Color(255,255,255) # background
brown=pygame.Color(165,42,42)   # food

# fps Controller
fpsController=pygame.time.Clock()

# Important Variables
snakePos=[100,50]
snakeBody=[[100,50],[90,50],[80,50]]
foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawm=True
score =0

direction='RIGHT'
changeTo=direction

# Game Over Function
def gameOver():
    myFont=pygame.font.SysFont('monaco',72)
    GOsurface=myFont.render('Game Over!',True,red)
    GOrect=GOsurface.get_rect()
    GOrect.midtop=(360,15)
    playSurface.blit(GOsurface,GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()   # pygame exit
    sys.exit(-1)    #console exit

# Score function
def showScore(choice=1):
    sFont=pygame.font.SysFont('monaco',30)
    ssurface=sFont.render('Score : {0}'.format(score),True,black)
    srect=ssurface.get_rect()
    if choice==1:
        srect.midtop = (80,10)
    else:
        srect.midtop = (360, 120)
    playSurface.blit(ssurface,srect)

# Main logic of the game
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(-1)
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo='RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo='LEFT'
            if event.key== pygame.K_UP or event.key == ord('w'):
                changeTo='UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo='DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation of direction
    if changeTo=='RIGHT' and not direction == 'LEFT':
        direction='RIGHT'
    if changeTo=='LEFT' and not direction == 'RIGHT':
        direction='LEFT'
    if changeTo=='UP' and not direction == 'DOWN':
        direction='UP'
    if changeTo=='DOWN' and not direction == 'UP':
        direction='DOWN'

    # Update snake position
    if direction=='RIGHT':
        snakePos[0]+=10
    if direction=='LEFT':
        snakePos[0]-=10
    if direction=='UP':
        snakePos[1]-=10
    if direction=='DOWN':
        snakePos[1]+=10

    # Snake body mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0]==foodPos[0] and snakePos[1]==foodPos[1]:
        score+=1
        foodSpawm=False
    else:
        snakeBody.pop()

    # Food spawn
    if foodSpawm==False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawm=True
    # Background color
    playSurface.fill(white)
    # Draw Snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))
    # Draw Food
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    # Bound
    if snakePos[0]>710 or snakePos[0]<0:
        gameOver()
    if snakePos[1]>450 or snakePos[1]<0:
        gameOver()
    # Self hit
    for block in snakeBody[1:]:
        if snakePos[0]==block[0] and snakePos[1]==block[1]:
            gameOver()

    showScore()
    pygame.display.flip()
    fpsController.tick(20)










