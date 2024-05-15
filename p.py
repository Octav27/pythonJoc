import pygame
import random
from enum import Enum


pygame.init()
HEIGHT = 800
WIDTH = 800


class Direction(Enum):
    LEFT=1
    UP=2
    RIGHT=3
    DOWN=4

class Obiect(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        pygame.sprite.Sprite.__init__(self)

        image_scale = 60/image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center =[x,y]
class Patron(Obiect):

    def __init__(self, width, height,  regular_speed, fast_speed):
        image = pygame.image.load('images/bullet.png')
        self.width = width
        self.height = height
        self.regular_speed = regular_speed
        self.fast_speed = fast_speed
       # self.rect = pygame.Rect((random.randint(0,WIDTH-self.width), random.randint(0,HEIGHT-self.height), self.width, self.height))
        super().__init__(image,(random.randint(0,WIDTH-self.width)),random.randint(0,HEIGHT-self.height) )

class Om(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        pygame.sprite.Sprite.__init__(self)

        image_scale = 45/ image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
class Player(Om):
    def __init__(self,x,y):
        image = pygame.image.load('images/player.png')
        super().__init__(image,x,y)
    


screen = pygame.display.set_mode((WIDTH, HEIGHT))


player_group = pygame.sprite.Group()
pl = Player(600,600)
player_group.add(pl)


ziduri_group = pygame.sprite.Group()

#player =pygame.Rect((350,550,50,50))
zid = pygame.Rect((random.randint(0,750),random.randint(0,750),50,50))

patroane = [Patron(50,50,4,9), Patron(50,50,4,9),Patron(50,50,4,9),Patron(50,50,4,9),Patron(50,50,4,9),Patron(50,50,4,9), Patron(50,50,4,9),Patron(50,50,4,9),Patron(50,50,4,9)]
ziduri_group.add(patroane)

speedPlayer = 5
speedPatron = 2
static = True
go =True

while go: 

    screen.fill((0,0,0))

    # pygame.draw.rect(screen,(255,0,0),player)
    player_group.draw(screen)
   # pygame.draw.rect(screen,(255,255,0), zid)
    for patron in patroane:
        ziduri_group.draw(screen)

        if static == False:
            patron.rect.move_ip(0,9)
        else:
            patron.rect.move_ip(0,random.randint(speedPatron,speedPatron+2)) 

        if patron.rect.y>HEIGHT:
            patron.rect.y = 0
            patron.rect.x = random.randint(0,WIDTH-50)
      #  if patron.colliderect(pl.rect):
         #   go=False

    
    if static == False:
        
        zid.move_ip(0,9)
        static = True

    else:
        zid.move_ip(0,speedPatron)


    pygame.time.wait(20)

    key = pygame.key.get_pressed()


    if key[pygame.K_a] ==True:
        if pl.rect.x >0:
            #player.move_ip(-1*speedPlayer,0)
            pl.rect.x -=5
            static=False
 
    elif key[pygame.K_d]== True:
        if pl.rect.x<WIDTH - pl.rect.width:
            #player.move_ip(speedPlayer,0)
            pl.rect.x +=5
            pl.image = pygame.transform.rotate(pl.image,90)
            static=False
    elif key[pygame.K_w]==True:
        if pl.rect.y>0:
           # player.move_ip(0,-1*speedPlayer)
            pl.rect.y -=5
            static=False
    elif key[pygame.K_s]==True:
        if pl.rect.y<HEIGHT - pl.rect.height:
            #player.move_ip(0,speedPlayer)
            pl.rect.y +=5
            static=False

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            go = False
    pygame.display.update()


pygame.quit()