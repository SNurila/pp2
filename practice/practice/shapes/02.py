import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
circle_rad = 50
color_circle = (0, 0, 0)
color_sq = (0, 0, 0)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    circle = pygame.draw.circle(screen, color_circle, (70, 150), circle_rad)
    square = pygame.draw.rect(screen, color_sq, (250, 100, 100, 100))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:
        if keys[pygame.K_r]:
            color_circle = (255, 0, 0)
            pygame.draw.circle(screen, color_circle, (70, 150), circle_rad)
        elif keys[pygame.K_y]:
            color_circle = (255, 255, 0)
            pygame.draw.circle(screen, color_circle, (70, 150), circle_rad)
        elif keys[pygame.K_b]:
            color_circle = (0, 0, 255)
            pygame.draw.circle(screen, color_circle, (70, 150), circle_rad)

    elif keys[pygame.K_s]:
        if keys[pygame.K_r]:
            color_sq = (255, 0, 0)
            pygame.draw.rect(screen, color_sq, (250, 100, 100, 100))
        elif keys[pygame.K_y]:
            color_sq = (255, 255, 0)
            pygame.draw.rect(screen, color_sq, (250, 100, 100, 100))
        elif keys[pygame.K_b]:
            color_sq = (0, 0, 255)
            pygame.draw.rect(screen, color_sq, (250, 100, 100, 100))

        
    pygame.display.flip()
