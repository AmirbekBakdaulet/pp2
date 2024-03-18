import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
x = 50
y = 50

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y= max(y-20,25)
        elif pressed[pygame.K_DOWN]: 
            y=min(y+20,300-25)
        if pressed[pygame.K_LEFT]: 
              x =max(x-20,25)
        elif pressed[pygame.K_RIGHT]: 
              x =min(x+20,400-25)
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen,(255,0,0),(x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)