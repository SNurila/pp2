import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for x in range(0, 400, 20):
        pygame.draw.line(screen, (0, 0, 255), (x, 0), (x, 300))

    for y in range(0, 300, 20):
        pygame.draw.line(screen, (0, 0, 255), (0, y), (400, y))

    pygame.display.flip()