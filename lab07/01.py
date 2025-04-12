import pygame
import math
import time

pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)

clock_face = pygame.image.load("/Users/nurilasalamat/Downloads/clock.png")
minute_hand = pygame.image.load("/Users/nurilasalamat/Downloads/min_hand.png")
second_hand = pygame.image.load("/Users/nurilasalamat/Downloads/sec_hand.png")


clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
minute_hand = pygame.transform.scale(minute_hand, (400, 640))  
second_hand = pygame.transform.scale(second_hand, (400, 640))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

def rotate_hand(image, angle):
    
    rotated_image = pygame.transform.rotate(image, -angle)  
    rect = rotated_image.get_rect(center = CENTER)
    return rotated_image, rect

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = (minutes % 60) * 6  
    second_angle = (seconds % 60) * 6  

    rotated_minute_hand, minute_rect = rotate_hand(minute_hand, minute_angle)
    rotated_second_hand, second_rect = rotate_hand(second_hand, second_angle)

    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))
    screen.blit(rotated_minute_hand, minute_rect)
    screen.blit(rotated_second_hand, second_rect)

    pygame.display.flip()
    clock.tick(1)  

pygame.quit()
