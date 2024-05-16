import pygame
import random
import button
from enum import Enum


pygame.init()
HEIGHT = 800
WIDTH = 800



#Clase
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

        image_scale = 75/ image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
class Player(Om):
    def __init__(self,x,y):
        image = pygame.image.load('images/player.png')
        super().__init__(image,x,y)



class ImagBack(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
      #  image_scale = 45/ image.get_rect().width
      #  new_width = image.get_rect().width * image_scale
      #  new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (WIDTH, HEIGHT))

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    

class Background(ImagBack):
     def __init__(self,x,y):
         image = pygame.image.load('images/back.png')
         super().__init__(image,x,y)
         
#Clase Sfarsit


screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_group = pygame.sprite.Group()
pl = Player(600,600)
pl.image = pygame.transform.rotate(pl.image,90)
player_group.add(pl)

font = pygame.font.Font('freesansbold.ttf', 20)
score_text  = font.render('Scorul: ', True,(0,0,0))
score_rect = score_text.get_rect()
score = 0
score_rect.x = 5
score_rect.y = 5

joaca_img  = pygame.image.load("images/button_joaca.png").convert_alpha()
joaca_button = button.Buton(304,125,joaca_img,1)
iesi_img = pygame.image.load("images/button_iesi.png").convert_alpha()
iesi_button = button.Buton(325, 225, iesi_img,1)

back_group = pygame.sprite.Group()
back = Background(WIDTH/2,HEIGHT/2)
back_group.add(back)

ziduri_group = pygame.sprite.Group()
zid = pygame.Rect((random.randint(0,750),random.randint(0,750),50,50))

patroane = [Patron(2,40,4,9), Patron(2,40,4,9),Patron(2,40,4,9),Patron(2,40,4,9),Patron(2,40,4,9),Patron(2,40,4,9), Patron(2,40,4,9),Patron(2,40,4,9),Patron(2,40,4,9)]
ziduri_group.add(patroane)

for p in patroane:
    p.image = pygame.transform.rotate(p.image, 180)

speedPlayer = 5
speedPatron = 2
static = True
go =True
game =False


while go: 
    score_text  = font.render('Scorul: '+str(score), True,(0,0,0))

    if game==   True:
        screen.fill((0,0,0))
        back_group.draw(screen)
        screen.blit(score_text, score_rect)
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
                score+=1
                patron.rect.x = random.randint(0,WIDTH-50)
            if patron.rect.colliderect(pl.rect):
                print(patron.rect.width)
                game=False

            
        if static == False:   
            zid.move_ip(0,9)
            static = True

        else:
            zid.move_ip(0,speedPatron)


        pygame.time.wait(20)
        key = pygame.key.get_pressed()

        if key[pygame.K_a] ==True:
            if pl.rect.x >0:
                pl.rect.x -=5
                static=False
        
        elif key[pygame.K_d]== True:
            if pl.rect.x<WIDTH - pl.rect.width:
                pl.rect.x +=5
                static=False
        if key[pygame.K_w]==True:
            if pl.rect.y>0:
                pl.rect.y -=5
                static=False
        elif key[pygame.K_s]==True:
            if pl.rect.y<HEIGHT - pl.rect.height:
                pl.rect.y +=5
                static=False

    else:
        screen.fill((255,255,255))
        if joaca_button.draw(screen):
            for patron in patroane :
                patron.rect.y = random.randint(0,HEIGHT-50)
                patron.rect.x = random.randint(0,WIDTH-50)

            game=True
        if iesi_button.draw(screen):
            go=False
     


    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            go = False
    pygame.display.update()
 
        



pygame.quit()