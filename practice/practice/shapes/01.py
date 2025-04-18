import pygame
import math
pygame.init()

screen = pygame.display.set_mode((400, 300))
caption = pygame.display.set_caption("Smiley face")
center = (200, 150)

circle_rad = 50


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), center, circle_rad + 5)
    pygame.draw.circle(screen, (255, 255, 0), center, circle_rad)
    pygame.draw.arc(screen, (0, 0, 0), (175, 150, 50, 25), math.pi, 0, 5)
    pygame.draw.circle(screen, (0, 0, 0), (175, 135), 10)
    pygame.draw.circle(screen, (0, 0, 0), (230, 135), 10)

    pygame.display.flip()
