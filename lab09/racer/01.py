import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.font.init()

FPS = 60
FramePerSec = pygame.time.Clock()


WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coin Racer")
background = pygame.image.load('/Users/nurilasalamat/Documents/pp2/lab09/racer/AnimatedStreet.png')

class Coin(pygame.sprite.Sprite):
    def __init__(self, image_path, weight):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (40, 40))
        self.rect = self.image.get_rect()
        self.weight = weight
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/nurilasalamat/Documents/pp2/lab09/racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("/Users/nurilasalamat/Documents/pp2/lab09/racer/Enemy.png"), (60, 60))
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Label:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw(self, surface):
        text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        surface.blit(text, (10, 10))

    def update_score(self, amount):
        self.score += amount

player = Player()
enemy = Enemy()
label = Label()


coins = pygame.sprite.Group(
    Coin("/Users/nurilasalamat/Documents/pp2/lab09/racer/Coin_gold.png", 1),
    Coin("/Users/nurilasalamat/Documents/pp2/lab09/racer/Coin_silver.png", 2),
    
)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    player.update()
    for coin in coins:
        coin.move()

    enemy.move()


    for coin in coins:
        if player.rect.colliderect(coin.rect):
            label.update_score(coin.weight)
            coin.reset()


    if label.score // 5 + 5 > enemy.speed:
        enemy.speed += 1


    if player.rect.colliderect(enemy.rect):
        print("Game Over! Final Score:", label.score)
        pygame.quit()
        sys.exit()


    
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background, (0, 0))
    player.draw(DISPLAYSURF)
    enemy.draw(DISPLAYSURF)
    for coin in coins:
        coin.draw(DISPLAYSURF)
    label.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
