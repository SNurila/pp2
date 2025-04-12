import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
ball_rad = 25
step = 20

ball_x, ball_y = 200, 150

done = False

while not done:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x - ball_rad - step >= 0:
        ball_x -= step
    if keys[pygame.K_RIGHT] and ball_x + ball_rad + step <= 400:
        ball_x += step
    if keys[pygame.K_UP] and ball_y - ball_rad -step >= 0:
        ball_y -= step
    if keys[pygame.K_DOWN] and ball_y +ball_rad + step <= 300:
        ball_y += step

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_rad)
    pygame.display.flip()