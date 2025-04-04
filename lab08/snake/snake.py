import pygame
import random
import sys
import os


pygame.init()


WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Maze Game")


SNAKE_COLOR = (12, 237, 211)
FOOD_COLOR = (255, 0, 0)
GRID_COLOR = (207, 203, 192)
BG_COLOR = (0, 0, 0)
WALL_COLOR = (100, 100, 100)
TEXT_COLOR = (255, 255, 255)


font = pygame.font.SysFont("Arial", 24)


clock = pygame.time.Clock()


snake = [(40, 40)]
dx, dy = 1, 0
step = CELL_SIZE


score = 0
level = 1
speed = 5


def load_maze(level_num):
    maze_file = f"/Users/nurilasalamat/Documents/pp2/lab08/snake/levels/level{level_num}.txt"
    walls = set()
    try:
        with open(maze_file, "r") as file:
            lines = file.readlines()
            for y, line in enumerate(lines):
                for x, char in enumerate(line.strip()):
                    if char == "#":
                        walls.add((x * CELL_SIZE, y * CELL_SIZE))
    except FileNotFoundError:
        print(f"Level {level_num} not found! Game over.")
        pygame.quit()
        sys.exit()
    return walls

walls = load_maze(level)

def place_food():
    while True:
        fx = random.randint(0, COLS - 1) * CELL_SIZE
        fy = random.randint(0, ROWS - 1) * CELL_SIZE
        if (fx, fy) not in snake and (fx, fy) not in walls:
            return fx, fy

food = place_food()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy != -1:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx != 1:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx != -1:
                dx, dy = 1, 0

    head_x, head_y = snake[-1]
    new_x = (head_x + dx * step) % WIDTH
    new_y = (head_y + dy * step) % HEIGHT
    new_head = (new_x, new_y)

    if new_head in snake or new_head in walls:
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    snake.append(new_head)

    if new_head == (food[0], food[1]):
        score += 1
        if score % 5 == 0:  
            level += 1
            speed += 1
            walls = load_maze(level)
        food = place_food()
    else:
        snake.pop(0)


    screen.fill(BG_COLOR)


    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))


    for wall in walls:
        pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(wall[0], wall[1], CELL_SIZE, CELL_SIZE))


    for block in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))


    pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))


    score_text = font.render(f"Score: {score}   Level: {level}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)
