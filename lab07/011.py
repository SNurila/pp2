import pygame
import time
pygame.init()

screen = pygame.display.set_mode((400, 300))
center = (400 // 2, 300 // 2)
done = False
clock = pygame.time.Clock()

clock_face = pygame.image.load("/Users/nurilasalamat/Downloads/clock.png")
minute_hand = pygame.image.load("/Users/nurilasalamat/Downloads/min_hand.png")
second_hand = pygame.image.load('/Users/nurilasalamat/Downloads/sec_hand.png')

clock_face = pygame.transform.scale(clock_face, (400, 300))
minute_hand = pygame.transform.scale(minute_hand, (300, 320))
second_hand = pygame.transform.scale(second_hand, (300, 320))

def rotate_hand(image, angle):
    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect(center = center)
    return rotated_image, rect
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    min_angle = (minutes % 60) * 6
    sec_angle = (seconds % 60) * 6

    rotated_min_hand, minute_rect = rotate_hand(minute_hand, min_angle)
    rotate_sec_hand, second_rect = rotate_hand(second_hand, sec_angle)

    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))
    screen.blit(rotated_min_hand, minute_rect)
    screen.blit(rotate_sec_hand, second_rect)

    pygame.display.flip()
    clock.tick(1)