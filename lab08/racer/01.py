import pygame, sys
from pygame.locals import *
import random
 
pygame.init() 
pygame.font.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
background = pygame.image.load("/Users/nurilasalamat/Desktop/pp2/lab08/racer/AnimatedStreet.png")
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("/Users/nurilasalamat/Desktop/pp2/lab08/racer/Coin.png"), (34, 34)) 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0) 
       
      def move(self, is_scored):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600) or (is_scored):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/nurilasalamat/Desktop/pp2/lab08/racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
   
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 

class Label(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0  
        self.font = pygame.font.SysFont('Comic Sans MS', 30)  

    def draw(self, surface):
        """Draw the score on the screen."""
        text_surface = self.font.render(f'Score: {self.score}', False, (0, 0, 0))
        surface.blit(text_surface, (10, 10))  

    def update_score(self, points):
        """Increase the score by a given amount."""
        self.score += points

         
P1 = Player()
C1 = Coin()
L1 = Label()

def check_score():
    if P1.rect.top <= C1.rect.bottom and P1.rect.left < C1.rect.right and P1.rect.right > C1.rect.left:
        L1.update_score(1)
        C1.move(True)
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    C1.move(False)
    check_score()
    
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background, (0, 0))
    P1.draw(DISPLAYSURF)
    C1.draw(DISPLAYSURF)
    L1.draw(DISPLAYSURF)    
    pygame.display.flip()
    FramePerSec.tick(FPS)
    

