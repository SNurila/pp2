import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
center = (200, 150)
image = pygame.image.load("/Users/nurilasalamat/Desktop/pp2/practice/practice/images/Player.png")
rect = image.get_rect(center= center)
angle = 0
rotate = False
done = False
while not done:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rotate = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                rotate = False
    if rotate:
        angle += 2
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center= center)
    screen.blit(image, new_rect)
    pygame.display.flip()
    clock.tick(60)