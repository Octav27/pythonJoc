import pygame
import random

pygame.init()

HEIGHT = 800
WIDTH = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player =pygame.Rect((350,550,50,50))
zid = pygame.Rect((random.randint(0,750),random.randint(0,750),50,50))

patroane = [pygame.Rect((random.randint(0,750),random.randint(0,750),50,50)),pygame.Rect((random.randint(0,750),random.randint(0,750),50,50)),pygame.Rect((random.randint(0,750),random.randint(0,750),50,50)),pygame.Rect((random.randint(0,750),random.randint(0,750),50,50)),pygame.Rect((random.randint(0,750),random.randint(0,750),50,50)),pygame.Rect((random.randint(0,750),random.randint(0,750),50,50)),pygame.Rect((random.randint(0,750),random.randint(0,750),50,50))]

speedPlayer = 5

speedPatron = 2

static = True


go =True

while go:

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,0,0),player)
    pygame.draw.rect(screen,(255,255,0), zid)
    for patron in patroane:
        pygame.draw.rect(screen,(random.randint(0,255), random.randint(0,255), random.randint(0,255)) ,patron)
        if static == False:
            patron.move_ip(0,9)
        else:
            patron.move_ip(0,random.randint(speedPatron,speedPatron+2)) 

        if patron.y>HEIGHT:
            patron.y = 0
            patron.x = random.randint(0,WIDTH-50)
    
    if static == False:
        
        zid.move_ip(0,9)
        static = True

    else:
        zid.move_ip(0,speedPatron)

    pygame.time.wait(20)

    key = pygame.key.get_pressed()


    if key[pygame.K_a] ==True:
        if player.x >0:
            player.move_ip(-1*speedPlayer,0)
            static=False
 
    elif key[pygame.K_d]== True:
        if player.x<WIDTH - player.width:
            player.move_ip(speedPlayer,0)
            static=False
    elif key[pygame.K_w]==True:
        if player.y>0:
            player.move_ip(0,-1*speedPlayer)
            static=False
    elif key[pygame.K_s]==True:
        if player.y<HEIGHT - player.height:
            player.move_ip(0,speedPlayer)
            static=False

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            go = False
    pygame.display.update()


pygame.quit()