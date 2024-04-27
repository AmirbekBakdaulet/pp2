import pygame
import datetime
import random
from  tasw import user_insert,find_user
pygame.init()


#function that draws lines
def drawlines(screen,HEIGHT,WIDTH,block):
    for i in range (0,HEIGHT+block,block):
        pygame.draw.line(screen,(255,255,255),(i,0),(i,WIDTH),1)
    for i in range (0,WIDTH+block,block):
        pygame.draw.line(screen,(255,255,255),(0,i),(HEIGHT,i),1)

class Point:  #function that allows us to initialize that in list we have not tuple,we have something that can be taken out by smth.x and smth.y
    def __init__(self,x,y):
        self.x=x
        self.y=y


class Snake:  #snake class
    snakebody=[] 
    def __init__(self):
        self.snakebody=[(Point(x=HEIGHT//2//BLOCK,y=WIDTH//2//BLOCK))] #initialize start position

    def draw(self):
        head=self.snakebody[0] #first block in list is head
        pygame.draw.rect(SCREEN,(0,255,0),pygame.Rect(head.x*BLOCK,head.y*BLOCK,BLOCK,BLOCK)) #draw
        for body in self.snakebody[1:]: #draw body,but start not from 0 ,start from 1
            pygame.draw.rect(SCREEN,(0,200,100),pygame.Rect(body.x*BLOCK,body.y*BLOCK,BLOCK,BLOCK))

    def move(self,dx,dy):
        for inx in range(len(self.snakebody)-1,0,-1):# change cordinates to the cordinates of previous in the list
            self.snakebody[inx].x=self.snakebody[inx-1].x
            self.snakebody[inx].y=self.snakebody[inx-1].y
        self.snakebody[0].x+=dx
        self.snakebody[0].y+=dy
        if self.snakebody[0].x>=HEIGHT//BLOCK:
            self.snakebody[0].x=0
        elif self.snakebody[0].x<0:
            self.snakebody[0].x=HEIGHT//BLOCK
        elif self.snakebody[0].y>=WIDTH//BLOCK:
            self.snakebody[0].y=0
        elif self.snakebody[0].y<0:
            self.snakebody[0].y=WIDTH//BLOCK

    def collision(self,foodx,foody): # checing colision with head of snake ond x,y cords
        if foodx==self.snakebody[0].x and foody==self.snakebody[0].y:
            return True
        return False
def timer_food():
    timer = int(datetime.datetime.now().second) + 3
    if timer>=60:
        timer-=60 
    return timer

class Food: #food.
    def __init__(self):
        self.x=random.randint(0,HEIGHT//BLOCK-1)
        self.y=random.randint(0,WIDTH//BLOCK-1)
        self.weight=random.randint(1,3)
        self.color=(0,0,0)
        self.timer = timer_food()
    def draw(self):
        if self.weight==1:
            self.color=(102,204,0)
        elif self.weight==2:
            self.color=(255,255,0)
        else:
            self.color=(255,0,0)
        for checking_walls in walls.wall_list:
            if food.x==checking_walls.x and food.y==checking_walls.y:
                self.x=random.randint(0,HEIGHT//BLOCK-1)
                self.y=random.randint(0,WIDTH//BLOCK-1)
        pygame.draw.circle(SCREEN,self.color,(self.x*BLOCK+BLOCK//2,self.y*BLOCK+BLOCK//2),BLOCK//2)
    def collision(self):
        for i in range(len(walls.wall_list)):
            for j in range(len(snake.snakebody)):
                if (snake.snakebody[j].x==food.x and snake.snakebody[j].y==food.y)or (walls.wall_list[i].x==food.x or walls.wall_list[i].y==food.y):
                    return True
        return False

class Walls:
    def __init__(self):
        self.x=0
        self.y=0
        self.wall_list=[Point(x=0,y=0)]
    def draw(self,level):
        if level==1:
            self.x=0
            self.y=0
            for i in range(0,WIDTH,BLOCK):  
               pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(self.x,i,BLOCK-5,BLOCK-5))
               self.wall_list.append(Point(self.x,i/BLOCK))
        elif level==2:
            self.x=0
            self.y=0
            for i in range(0,WIDTH,BLOCK):  
               pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(self.x,i,BLOCK-5,BLOCK-5))
               pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(self.x+WIDTH-BLOCK,i,BLOCK-5,BLOCK-5))
               self.wall_list.append(Point(self.x,i/BLOCK))
               self.wall_list.append(Point(self.x+WIDTH//BLOCK-1,i/BLOCK))
            for i in range(0,HEIGHT,BLOCK):  
               pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(i,self.y,BLOCK-5,BLOCK-5))
               pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(i,self.y+HEIGHT-BLOCK,BLOCK-5,BLOCK-5))
               self.wall_list.append(Point(i/BLOCK,self.y//BLOCK))
               self.wall_list.append(Point(i/BLOCK,self.y//BLOCK+HEIGHT//BLOCK-1))
            
        else:
            self.x=WIDTH//2
            self.y=HEIGHT//2
            self.wall_list.clear()
            self.wall_list=[Point(x=self.x,y=0)]
            for i in range(0,WIDTH,BLOCK):  
               pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(self.x,i,BLOCK-5,BLOCK-5))
               self.wall_list.append(Point(self.x//BLOCK,i/BLOCK))
            for i in range(0,HEIGHT,BLOCK):  
               pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(i,self.y,BLOCK-5,BLOCK-5))
               self.wall_list.append(Point(i/BLOCK,self.y//BLOCK))

class Bomb:
    def __init__(self):
        self.x=random.randint(0,HEIGHT//BLOCK-1)
        self.y=random.randint(0,WIDTH//BLOCK-1)
    def draw(self):
        pygame.draw.circle(SCREEN,(150,255,255),(self.x*BLOCK+BLOCK//2,self.y*BLOCK+BLOCK//2),BLOCK//2)


runned,inserted=True,False
initial_level=1
firsttime=True
WIDTH,HEIGHT,BLOCK=700,700,50
clock=pygame.time.Clock()
dx,dy=0,0
level=1
score2=0
saved_lenght=0
SCREEN=pygame.display.set_mode((HEIGHT,WIDTH))
font = pygame.font.SysFont("Verdana", 30)
font2 = pygame.font.SysFont("Verdana", 60)
button=font2.render("exit",True,(200,200,0))
game_over = font.render("Game Over", True, (0,0,0))
snake=Snake()
food=Food()
walls=Walls()
bomb=Bomb()
name=''
stoped=False

while not inserted:

    SCREEN.fill((0,0,0))
    insert_text=font.render("your name:",True,(255,255,255))
    SCREEN.blit(insert_text,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            inserted=True
            runned=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                name=name[:-1]
            elif event.key==pygame.K_RETURN:
                inserted=True
            else:
                key_name = pygame.key.name(event.key)
                name+=f'{key_name}'
    nametext=font.render(f"{name}",True,(255,255,255))
    SCREEN.blit(nametext,(200,0))
            

    pygame.display.flip()
while runned:
    SCREEN.fill((0,0,0))
    user_name=name
    if find_user(user_name)==0 and firsttime==True:
        score=score2
    elif  find_user(user_name)!=0 and firsttime==True:
        score2=find_user(user_name)//10*10
        score=score2
        firsttime=False
    
    drawlines(SCREEN,HEIGHT,WIDTH,BLOCK)#draw grid
    for event in pygame.event.get():#check quit event and buttons to control
        if event.type==pygame.QUIT:
            runned=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                dx,dy=0,-1
                stoped=False
            elif event.key==pygame.K_RIGHT:
                dx,dy=1,0
                stoped=False
            elif event.key==pygame.K_LEFT:
                dx,dy=-1,0
                stoped=False
            elif event.key==pygame.K_DOWN:
                dx,dy=0,1
                stoped=False
            elif event.key==pygame.K_SPACE:
                dx,dy=0,0
                stoped=True
    #give dx dy to snake class
    if stoped:
        pass
    else:
        snake.move(dx,dy)

    for i in range(1,len(snake.snakebody)):#check collision with itself
        if snake.collision(snake.snakebody[i].x,snake.snakebody[i].y):
            runned=False
    if datetime.datetime.now().second==food.timer:#timer to food
        food.x=random.randint(0,HEIGHT//BLOCK-1)
        food.y=random.randint(0,WIDTH//BLOCK-1)
        food.weight=random.randint(1,3)
        if food.collision():#check collision food with walls and snakebody
            food.x=random.randint(0,HEIGHT//BLOCK-1)
            food.y=random.randint(0,WIDTH//BLOCK-1)
            food.timer=timer_food()

    level=score2//10+1
    if initial_level!=level:
        dx=0
        dy=0
        snake.snakebody.clear()
        snake.snakebody=[(Point(x=HEIGHT//2//BLOCK-3,y=WIDTH//2//BLOCK-3))]
        initial_level=level
    #draw all

    food.draw()
    bomb.draw()
    snake.draw()
    walls.draw(level)
    
    #score fonts and display

    #speed increasing by level
    x=5+level//3
    level_see=font.render(f"level: {level}",True,(255,255,255))
    score_see=font.render(f"score: {score2}",True,(255,255,255))
    SCREEN.blit(level_see,(0,0))
    SCREEN.blit(score_see,(HEIGHT-150,0))
    #check collision of snake with food
    if snake.collision(food.x,food.y):
        for weight in range(food.weight):
            snake.snakebody.append(Point(food.x,food.y))
        food.x=random.randint(0,HEIGHT//BLOCK-1)
        food.y=random.randint(0,WIDTH//BLOCK-1)
        score2+=food.weight
        food.weight=random.randint(1,3)
        food.timer=timer_food()
        if food.collision():
            food.x=random.randint(0,HEIGHT//BLOCK-1)
            food.y=random.randint(0,WIDTH//BLOCK-1)

    if snake.collision(bomb.x,bomb.y):
        snake.snakebody.pop()
        while len(snake.snakebody)==0:
            SCREEN.fill((255,0,0))
            SCREEN.blit(game_over, SCREEN.get_rect().center)
            pygame.draw.rect(SCREEN,(0,255,0),pygame.Rect(200,200,50,50),0)
            #SCREEN.blit(SCREEN)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0]>200 and pygame.mouse.get_pos()[0]<250) and (pygame.mouse.get_pos()[1]>200 and pygame.mouse.get_pos()[1]<250) :
                    pygame.quit()
                if event.type==pygame.QUIT:
                    pygame.quit()

        bomb.x=random.randint(0,HEIGHT//BLOCK-1)
        bomb.y=random.randint(0,WIDTH//BLOCK-1)
        for i in range(len(walls.wall_list)):
            for j in range(len(snake.snakebody)):
                if (snake.snakebody[j].x==bomb.x and snake.snakebody[j].y==bomb.y)or (walls.wall_list[i].x==bomb.x or walls.wall_list[i].y==bomb.y):
                    bomb.x=random.randint(0,HEIGHT//BLOCK-1)
                    bomb.y=random.randint(0,WIDTH//BLOCK-1)


    for i in range(len(walls.wall_list)):#check collision with walls and snakehead
        if snake.collision(walls.wall_list[i].x,walls.wall_list[i].y):
            runned=False
    if runned==False:
        record=(user_insert(user_name,score2))
        print(record)
    pygame.display.flip()
    clock.tick(x)
