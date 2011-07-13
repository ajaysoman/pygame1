import sys
import pygame
import random

pygame.init()
yellow = 255, 255, 0 
white = [255,255,255]
x_coord = 200
y_coord = 440
basicfont = pygame.font.Font('freesansbold.ttf',32)
youloss = basicfont.render("You Lose   Game Over",5,yellow)
youwon = basicfont.render("You Won   Game Over",5,yellow)
scoreboard = pygame.font.Font(None, 32)
size = [400,480]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Race Mania")
road = pygame.image.load("Road.jpg")
roadrect = road.get_rect()
enemies = []
energy = []
enemyhit = pygame.mixer.Sound("hit.wav")
energyhit = pygame.mixer.Sound("energy.wav")
for i in range(15):
    x=random.randrange(0,400)
    y=random.randrange(0,440)
    enemies.append([x,y])
for i in range(4):
    x=random.randrange(0,400)
    y=random.randrange(0,440)
    energy.append([x,y])
clock = pygame.time.Clock()
score = 0
done=False
while done==False:
    screen.blit(road, [0,0])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        move_x=0
        move_y=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x_coord>0:
                    move_x = -20
                    move_y = 0
                else:
                    move_x = 0
                    move_y = 0 
            if event.key == pygame.K_RIGHT:
                if x_coord<360:
                    move_x = 20
                    move_y = 0
                else:
                    move_x = 0
                    move_y = 0
        x_coord = x_coord+move_x
        y_coord = y_coord+move_y
    car = pygame.image.load("Car1.gif")
    screen.blit(car, [x_coord,y_coord])
    carrect = pygame.Rect(x_coord,y_coord,32,32 )
    car.set_colorkey(white)
    pygame.display.flip()
    for i in range(len(enemies)):
        enemies_im=pygame.image.load("enemies.gif").convert()
        screen.blit(enemies_im,enemies[i])
        enemies_im.set_colorkey(white)
        enemies[i][1]+=1
        if enemies[i][1] > 480:
            y=random.randrange(-480,-10)
            enemies[i][1]=y
            x=random.randrange(0,400)
            enemies[i][0]=x

        if carrect.collidepoint(enemies[i][0], enemies[i][1]):
            enemyhit.play()
            score = score - 3
            if score <=-5:
                screen.blit(youloss, [0,240])
                pygame.display.flip()
                sys.exit(1)
            y = random.randrange(-480,-10)
            enemies[i][0] = y
            x=random.randrange(0,480)
            enemies[i][1] = x
            
    for i in range(len(energy)):
        energy_im=pygame.image.load("energy.gif").convert()
        screen.blit(energy_im,energy[i])
        energy_im.set_colorkey(white)
        energy[i][1]+=1
        if energy[i][1] > 480:
            y=random.randrange(-480,-10)
            energy[i][1]=y
            x=random.randrange(0,400)
            energy[i][0]=x

        if carrect.collidepoint(energy[i][0], energy[i][1]):
            energyhit.play()
            score = score + 1
            if score >=25:
                screen.blit(youwon, [0,240])
                pygame.display.flip()
                sys.exit(1)

            y = random.randrange(-480,-10)
            energy[i][0] = y
            x=random.randrange(0,480)
            energy[i][1] = x
            
        screen.blit(scoreboard.render("Score " + str(score) , 4, (255,255,255)) , [40,40])
        pygame.display.flip()
    pygame.display.flip()
    clock.tick(1000)
             
pygame.quit ()
