import pygame
import sys
import random


pygame.init()
WIDTH = 600
HEIGHT = 400
GRID_SIZE = 20 


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


score = 0
level = 1
speed = 10
game_over = False


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.body = [((WIDTH / 2), (HEIGHT / 2))]  
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])  

    
    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= GRID_SIZE
        elif self.direction == "DOWN":
            y += GRID_SIZE
        elif self.direction == "LEFT":
            x -= GRID_SIZE
        elif self.direction == "RIGHT":
            x += GRID_SIZE
        self.body.insert(0, (x, y))
        self.body.pop() 

   
    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    # Check for collision with food
    def eat_food(self, food):
        if self.body[0] == food.position:
            self.body.append(self.body[-1]) 
            return True
        return False


    def check_collision(self):
        x, y = self.body[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True 
        for segment in self.body[1:]:
            if self.body[0] == segment:
                return True 
        return False


    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))


class Food:
    def __init__(self):
        self.position = self.generate_position()

  
    def generate_position(self):
        while True:
            x = random.randrange(0, WIDTH, GRID_SIZE)
            y = random.randrange(0, HEIGHT, GRID_SIZE)
            if (x, y) not in snake.body:
                return (x, y)


    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Draw score and level
def draw_score_level():
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: " + str(score), True, WHITE)
    level_text = font.render("Level: " + str(level), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

# Main game loop
snake = Snake()
food = Food()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

 
    snake.move()

 
    if snake.check_collision():
        game_over = True

   
    if snake.eat_food(food):
        score += 1
        if score % 3 == 0:  # Increase level every 3 foods eaten
            level += 1
            speed += 2  
        food.position = food.generate_position() 

   
    screen.fill(BLACK)

 
    snake.draw()
    food.draw()


    draw_score_level()


    pygame.display.update()


    clock.tick(speed)

#gmaeover
font = pygame.font.SysFont(None, 50)
game_over_text = font.render("Game Over!", True, WHITE)
screen.blit(game_over_text, (WIDTH/2 - 100, HEIGHT/2))
pygame.display.update()


pygame.time.wait(2000)
pygame.quit()
sys.exit()