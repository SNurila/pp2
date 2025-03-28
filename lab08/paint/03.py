import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    drawing_mode = "line"  # "line", "rect", "circle", "eraser"
    points = []
    rect_start = None
    circle_start = None

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
                
                # Color selection
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

                # Drawing modes
                elif event.key == pygame.K_t:
                    drawing_mode = "rect"
                    rect_start = None
                elif event.key == pygame.K_c:
                    drawing_mode = "circle"
                    circle_start = None
                elif event.key == pygame.K_l:
                    drawing_mode = "line"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click to increase radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # Right click to decrease radius
                    radius = max(1, radius - 1)

                if drawing_mode == "rect":
                    rect_start = event.pos
                elif drawing_mode == "circle":
                    circle_start = event.pos

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if drawing_mode == "line" or drawing_mode == "eraser":
                    points.append((position, mode if drawing_mode != "eraser" else "eraser"))
                    points = points[-256:]  # Limit to 256 points
        
        screen.fill((0, 0, 0))

        # Draw lines
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i][0], points[i + 1][0], radius, points[i][1])
            i += 1

        # Draw rectangle
        if drawing_mode == "rect" and rect_start:
            current_pos = pygame.mouse.get_pos()
            rect_width = current_pos[0] - rect_start[0]
            rect_height = current_pos[1] - rect_start[1]
            pygame.draw.rect(screen, colors[mode], (rect_start[0], rect_start[1], rect_width, rect_height), 2)

        # Draw circle
        if drawing_mode == "circle" and circle_start:
            current_pos = pygame.mouse.get_pos()
            radius = int(((current_pos[0] - circle_start[0]) ** 2 + (current_pos[1] - circle_start[1]) ** 2) ** 0.5)
            pygame.draw.circle(screen, colors[mode], circle_start, radius, 2)

        pygame.display.flip()
        clock.tick(60)

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
