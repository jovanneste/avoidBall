import pygame
import random
import numpy as np
 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 255)
RED = (255, 0, 0)

pygame.init()
 
ballspeed = 1.5

size = [500, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Game")
pygame.mouse.set_visible(0)
 
pygame.init()

x_speed = 0
y_speed = 0
x_coord = 250
y_coord = 400
    
done = False

rand_x = random.randint(1, 500)
rand_y = 0
rand_x2 = random.randint(1, 500)
rand_y2 = 0
    
clock = pygame.time.Clock()
   
points = 0  

font = pygame.font.SysFont(None, 25)

def message(msg, colour):
    screen_text = font.render(msg, True, colour)
    screen.blit(screen_text, [125, 230])
        
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True    
        
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                 x_speed = -6
             elif event.key == pygame.K_RIGHT:
                 x_speed = 6
             elif event.key == pygame.K_UP:
                 y_speed = -6
             elif event.key == pygame.K_DOWN:
                 y_speed = 6     
     
        elif event.type == pygame.KEYUP:
                
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 x_speed = 0
             elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 y_speed = 0

    if x_coord >= 500 or x_coord < 0 or y_coord >= 500 or y_coord < 0:
        done = True

    
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    
    rand_y += ballspeed 
    rand_y2 += ballspeed
    

    screen.fill(BLACK)

    pygame.draw.ellipse(screen, RED, [rand_x, rand_y, 30, 30])
    pygame.draw.ellipse(screen, RED, [x_coord, y_coord, 30, 30])
    pygame.draw.ellipse(screen, YELLOW, [rand_x2, rand_y2, 30, 30])
    if rand_y > 500:
        rand_x = random.randint(1, 500)
        rand_y = 0
    if rand_y2 > 500:
        rand_x2 = random.randint(1, 500)
        rand_y2 = 0        
    pygame.display.flip()
    
    def detectCollisions(x1,y1,x2,y2):
        if np.sqrt((x1-x2)**2+(y1-y2)**2)<30:
            return True

        
    collision = detectCollisions(rand_x,rand_y,x_coord,y_coord)
    if collision == True:
        rand_x = random.randint(1, 500)
        rand_y = 0
        points += 1
    collision2 = detectCollisions(rand_x2,rand_y2,x_coord,y_coord)
    if collision2 == True:
        done = True
        
    if done == True:
        screen.fill(WHITE)
        message("Game over, you scored " + str(points) + " points", RED)
        pygame.display.update()

     
    ballspeed += 0.005 
        
        
    clock.tick(60)
 
pygame.quit()





