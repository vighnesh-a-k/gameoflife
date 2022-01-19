from signal import raise_signal
import pygame
import numpy as np
import random
col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)


def life(screen,present,sz):
    count=0
    future=np.zeros((present.shape[0], present.shape[1]))
    for r,c in np.ndindex(present.shape):
        alive=np.sum(present[r-1:r+2,c-1:c+2])-present[r,c]
        if (alive<2 or alive>3) and (present[r,c]==1):
            col=col_about_to_die
        elif ( ((alive==2 or alive==3) and present[r,c]==1) or (present[r,c]==0 and alive==3)):
            col=col_alive
            future[r,c]=1
            count=count+1
        
        if present[r,c]==0:
                col=col_background
        else:
                col=col
        pygame.draw.rect(screen, col, (c*sz, r*sz, sz-1, sz-1))
    return future
    

def birth(x,y):
    cells = np.zeros((y, x))
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j]=int(random.randint(0, 7)/5)
            
    return cells
            
pygame.init()
present=birth(100,100)
x=70
y=70
surface = pygame.display.set_mode((x * 8, y * 8))  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    surface.fill(col_grid)
    present = life(surface, present, 8)
    
    pygame.display.update()








