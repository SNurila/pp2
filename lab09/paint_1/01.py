import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    drawing_mode = "line"  # Options: line, rect, circle, eraser, square, right_triangle, equilateral_triangle, rhombus
    points = []
    shape_start = None

    colors = {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128),
        'eraser': (0, 0, 0)
    }

    while True:
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                elif event.key == pygame.K_p:
                    mode = 'purple'
                elif event.key == pygame.K_e:
                    drawing_mode = "eraser"

               
                elif event.key == pygame.K_t:
                    drawing_mode = "rect"
                elif event.key == pygame.K_c:
                    drawing_mode = "circle"
                elif event.key == pygame.K_l:
                    drawing_mode = "line"
                elif event.key == pygame.K_s:
                    drawing_mode = "square"
                elif event.key == pygame.K_1:
                    drawing_mode = "right_triangle"
                elif event.key == pygame.K_2:
                    drawing_mode = "equilateral_triangle"
                elif event.key == pygame.K_3:
                    drawing_mode = "rhombus"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)

                shape_start = event.pos  

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if drawing_mode in ["line", "eraser"]:
                    points.append((position, mode if drawing_mode != "eraser" else "eraser"))
                    points = points[-256:]

        screen.fill((0, 0, 0))

      
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i][0], points[i + 1][0], radius, points[i][1])
            i += 1

       
        if shape_start:
            current_pos = pygame.mouse.get_pos()
            draw_shape(screen, drawing_mode, shape_start, current_pos, colors[mode])

        pygame.display.flip()
        clock.tick(60)

def draw_shape(screen, mode, start, end, color):
    x1, y1 = start
    x2, y2 = end
    width = x2 - x1
    height = y2 - y1

    if mode == "rect":
        pygame.draw.rect(screen, color, (x1, y1, width, height), 2)
    elif mode == "circle":
        radius = int(math.hypot(width, height))
        pygame.draw.circle(screen, color, start, radius, 2)
    elif mode == "square":
        side = min(abs(width), abs(height))
        pygame.draw.rect(screen, color, (x1, y1, side * (1 if width >= 0 else -1), side * (1 if height >= 0 else -1)), 2)
    elif mode == "right_triangle":
        pygame.draw.polygon(screen, color, [(x1, y1), (x2, y2), (x1, y2)], 2)
    elif mode == "equilateral_triangle":
        side = min(abs(width), abs(height))
        height = int((3 ** 0.5 / 2) * side)
        pygame.draw.polygon(screen, color, [(x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - height)], 2)
    elif mode == "rhombus":
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        pygame.draw.polygon(screen, color, [
            (center_x, y1), (x2, center_y), (center_x, y2), (x1, center_y)
        ], 2)

def drawLineBetween(screen, index, start, end, width, color_mode):
    colors = {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128),
        'eraser': (0, 0, 0)
    }

    color = colors[color_mode] if color_mode in colors else (255, 255, 255)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
