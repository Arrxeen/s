from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption("dd")
bullets= sprite.Group()
score = 0 
score1 = 0
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire = mixer.Sound("fire.ogg")

class GameSprite (sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, player_speed,width,height): 
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height)) 
        self.speed = player_speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y 
        self.width = width
        self.height = height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys= key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < 650: #650
            self.rect.x += self.speed
        if keys [K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 450: #450
            self.rect.y += self.speed
    def shot(self):
        bullet = Bullet("bullet.png",self.rect.x+15,self.rect.y,10,32,50)
        bullets.add(bullet)

class Enemy(GameSprite): 
    
    def update(self):
        global score1
        self.rect.y += 5
        if self.rect.y > 500:
            self.rect.x = randint(80,600)
            self.rect.y = 0
            score1 =  score1 + 1

class Enemy(GameSprite): 
    
    def update(self):
        self.rect.y += 5
        if self.rect.y > 500:
            self.rect.x = randint(80,600)
            self.rect.y = 0

    
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0 :
            self.kill()




background = transform.scale(image.load("galaxy.jpg"), (700,600))
# змінна ігорового циклу
game = True
clock = time.Clock()
FPS = 120
finish = False
monsters = sprite.Group()
monsters2 = sprite.Group()
for i in range(1,6):
    monster = Enemy("ufo.png",  randint(80,600),-50,randint(1,5),60 , 60 )
    monsters.add(monster)
font.init()


ship = Player("rocket.png", 300 , 400,25,50 ,90)
font2 = font.SysFont("Arial",50)
font1 = font.SysFont("Arial",80)
win = font1.render("Win!",True,(255,255,255))
lose = font1.render("Lode",True,(255,0,0))



while game:
    

    
    

    if finish != True:
        window.blit(background,(0,0))
        text = font2.render("Cчет:"+str(score),1,(255,255,255))
        window.blit(text,(10,20))

        text_lose = font2.render("Пропуск"+str(score1),1,(255,255,255))
        window.blit(text_lose,(10,50))



        ship.reset()
        ship.update()
        monsters.draw(window)
        monsters.update()
        bullets.draw(window)
        bullets.update()
        collides = sprite.groupcollide(monsters,bullets,True,True)
        for c in collides:
            monster = Enemy("ufo.png",  randint(80,600),-50,randint(1,5),60 , 60 )
            monsters.add(monster)
            score = score + 1
        if sprite.spritecollide(ship,monsters,False) or score1 >= 3 :
            finish = True
            text_l = font2.render("lose",1,(255,255,255))
            window.blit(text_l,(100,200))

        if score >= 10:
            finish = True
            text_w = font2.render("Win",1,(255,255,255))
            window.blit(text_w,(100,200))

    for e in event.get():
        
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.shot()
                fire.play()


    display.update()
    time.delay(60)
    clock.tick(FPS)