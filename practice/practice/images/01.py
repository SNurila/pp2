import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Loader")

def load_image(path):
    try:
        image = pygame.image.load(path)
        print(f"Loaded: {path}, Size: {image.get_size()}")
        return image
    except pygame.error as e:
        print(f"Failed to load image: {path}")
        print(f"Error: {e}")
        return None

done = False
current_image = None  # Store the currently selected image

while not done:
    screen.fill((255, 255, 255))  # Clear the screen each frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_image = load_image('/Users/nurilasalamat/Desktop/pp2/practice/practice/images/AnimatedStreet.png')
            elif event.key == pygame.K_2:
                current_image = load_image('/Users/nurilasalamat/Desktop/pp2/practice/practice/images/ball.png')
            elif event.key == pygame.K_3:
                current_image = load_image('/Users/nurilasalamat/Desktop/pp2/practice/practice/images/Coin_silver.png')
            elif event.key == pygame.K_4:
                current_image = load_image('/Users/nurilasalamat/Desktop/pp2/practice/practice/images/Enemy.png')
            elif event.key == pygame.K_5:
                current_image = load_image('/Users/nurilasalamat/Desktop/pp2/practice/practice/images/Player.png')

    if current_image:
        screen.blit(current_image, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()
