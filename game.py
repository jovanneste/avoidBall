import os
# hide pygame messsages to cmd line
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
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

print("\n\nLoading game...\n")
 
# initial ball speed
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
        # move ball in correct direction
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

    # update coordinates 
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    
    rand_y += ballspeed 
    rand_y2 += ballspeed
    

    screen.fill(BLACK)

    # show balls 
    pygame.draw.ellipse(screen, RED, [rand_x, rand_y, 30, 30])
    pygame.draw.ellipse(screen, RED, [x_coord, y_coord, 30, 30])
    pygame.draw.ellipse(screen, YELLOW, [rand_x2, rand_y2, 30, 30])
    if rand_y > 500:
        # dropping ball from a random place at the top of the screen
        rand_x = random.randint(1, 500)
        rand_y = 0
    if rand_y2 > 500:
        # dropping ball from a random place at the top of the screen
        rand_x2 = random.randint(1, 500)
        rand_y2 = 0        
    pygame.display.flip()
    
    # uses distance formula to check if there's a collision
    def detectCollisions(x1,y1,x2,y2):
        if np.sqrt((x1-x2)**2+(y1-y2)**2)<30:
            return True

        
    collision = detectCollisions(rand_x,rand_y,x_coord,y_coord)
    # if ball hits the yellow ball we increment the points
    if collision:
        rand_x = random.randint(1, 500)
        rand_y = 0
        points += 1
        print("Points: " + str(points))
    collision2 = detectCollisions(rand_x2,rand_y2,x_coord,y_coord)

    if collision2:
    # if ball hits the red ball the game ends
        done = True
    
    # game over
    if done == True:
        screen.fill(WHITE)
        message("Game over, you scored " + str(points) + " points", RED)
        pygame.display.update()

    # if game not over, increase the speed of the ball
    ballspeed += 0.005 
        
    clock.tick(60)
 


print("\nGame over, you scored " + str(points) + " points\n")


