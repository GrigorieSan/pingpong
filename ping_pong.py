from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))


rocketl = Player("racket.png", 50, 250, 10, 50, 150)
rocketr = Player("racket.png", 500, 250, 10, 50, 150)

tennis_ball = GameSprite("tenis_ball.png", 300, 250, 10, 50, 50)
speed_x = 3
speed_y = 3

 
run = True
finish = False
clock = time.Clock()
FPS = 60
 
 
while run:

    window.fill(back)

    tennis_ball.reset()

    rocketl.reset()
    rocketr.reset()

    rocketl.update_l()
    rocketr.update_r()
    tennis_ball.rect.x += speed_x
    tennis_ball.rect.y += speed_y

    for e in event.get():
        if e.type == QUIT:
           run = False

    if sprite.collide_rect(rocketl, tennis_ball) or sprite.collide_rect(rocketr, tennis_ball):
        speed_x *= -1
        speed_y *= -1

    
  
    
    display.update()
    clock.tick(FPS)