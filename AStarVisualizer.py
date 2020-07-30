from pygame.locals import *
import numpy as np
from random import randint
import pygame
import module


rule = 30
rotateRules = True

#Define Number of Columns
columns = 159
rows = 75

#Define Cell Sizes
WIDTH = 10
HEIGHT = 10
MARGIN = WIDTH // 5

#Define Colors
WHITE = (155, 155, 155)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)




cells = [[module.Cell for i in range(rows)] for j in range(columns)]


for row in range(0, rows):
    for column in range(0, columns):
        cells[column][row]  = (module.Cell(row, column))

for row in range(0, rows):
    for column in range(0, columns):
        print(cells[column][row].row,cells[column][row].column)

window_height = (((HEIGHT + MARGIN) * rows) + MARGIN) 
window_width = (((WIDTH + MARGIN) * columns) + MARGIN)

screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Cellular Automata - Rule ' + str(rule))


module.StartSim(cells, rows, columns)
module.RunSim(cells, rows, columns, rule)

grid = []
for row in range(6):
    grid.append([])
    for column in range(8):
        grid[row].append(0)

#pygame.init()

running = True

clock = pygame.time.Clock()

tick_count = 0

row_step = 0

pause = False

speed = 41

#Main pygame loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False  # Exit loop/ close pygame when x is clicked
        key=pygame.key.get_pressed()  #checking pressed keys
        if key[pygame.K_RETURN]: 
            row_step = 0
        if key[pygame.K_SPACE]:
            if pause: pause = False
            else: pause = True 
        if key[pygame.K_DOWN]:
            speed = int(speed * 2)
        if key[pygame.K_UP]:
            if speed > 1:
                speed = int(speed * .75)

        if key[pygame.K_LEFT]:
            rule -= 1
        if key[pygame.K_RIGHT]:
            rule += 1



    

    screen.fill(GREY)

    #update next row every 20 ticks
    if not pause:
        if (tick_count) % speed == 0:
            row_step += 1

    for row in range(0, rows):
        for column in range(0, columns):
            if row <= row_step:
                if cells[column][row].color == 0:
                    color = WHITE
                elif cells[column][row].color == 1:
                    color = BLACK
                else:
                    color = GREY
                pygame.draw.rect(screen,
                    color,
                    [(MARGIN + WIDTH) * cells[column][row].column + MARGIN,
                    (MARGIN + HEIGHT) * cells[column][row].row + MARGIN,
                    WIDTH, HEIGHT])
            else:
                color = GREY
                pygame.draw.rect(screen,
                    color,
                    [(MARGIN + WIDTH) * cells[column][row].column + MARGIN,
                    (MARGIN + HEIGHT) * cells[column][row].row + MARGIN,
                    WIDTH, HEIGHT])


    if row_step == rows:
        row_step = 0
        if rotateRules:
            if rule <= 255:
                rule += 1
                pygame.display.set_caption('Cellular Automata - Rule ' + str(rule))
                module.StartSim(cells, rows, columns)
                module.RunSim(cells, rows, columns, rule)
            else:
                rule = 0
        else:
            pygame.display.set_caption('Cellular Automata - Rule ' + str(rule))
            module.StartSim(cells, rows, columns)
            module.RunSim(cells, rows, columns, rule)
    tick_count += 1
    clock.tick(60)
   
    pygame.display.flip()