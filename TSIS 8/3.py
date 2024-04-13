import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    drawing = False
    tool = 'pencil'  
    
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
                elif event.key == pygame.K_p:
                    tool = 'pencil'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_q:
                    tool = 'rectangle'
                elif event.key == pygame.K_k:
                    tool = 'krestik'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    drawing = True
                    if tool == 'circle':
                        pygame.draw.circle(screen,mode, event.pos, radius)
                    elif tool == 'rectangle':
                        pygame.draw.rect(screen, mode, (event.pos[0], event.pos[1], radius * 2, radius * 2))
                    elif tool == 'krestik':
                        pygame.draw.line(screen,mode,(event.pos[0]-radius,event.pos[1]-radius),(event.pos[0]+radius, event.pos[1]+radius),5)
                        pygame.draw.line(screen,mode,(event.pos[0]-radius,event.pos[1]+radius),(event.pos[0]+radius, event.pos[1]-radius),5)
            if event.type == pygame.MOUSEBUTTONUP and tool=='eraser':
                drawing = False
            
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if tool == 'pencil':
                        position = event.pos
                        points = points + [position]
                        points = points[-256:]
                        i = 0
                        while i < len(points) - 1:
                            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                            i += 1
                    elif tool == 'eraser':
                        pygame.draw.circle(screen,(0,0,0), event.pos, radius)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
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
