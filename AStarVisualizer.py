from pygame.locals import *
import numpy as np
from random import randint
import pygame
import module

blank = False
rotateRules = False
randomize = False


#Define Number of Columns
columns = 30
rows = 30
#Define Cell Sizes
WIDTH = 20
HEIGHT = 20
MARGIN = WIDTH // 5

#Define Colors
WHITE = (255, 255, 255)
LIGHT_GREY = (155, 155, 155)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
GREEN = (0,128,0)
RED = (255,0,0)
BLUE = (0, 0, 255)




cells = [[module.Cell for i in range(rows)] for j in range(columns)]


for row in range(0, rows):
    for column in range(0, columns):
        cells[column][row]  = (module.Cell(row, column))


window_height = (((HEIGHT + MARGIN) * rows) + MARGIN) 
window_width = (((WIDTH + MARGIN) * columns) + MARGIN)

screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Conways Game of Life')

if randomize:
    module.StartRandom(cells, rows, columns)
elif blank:
    module.StartBlank(cells, rows, columns)
else:
    module.StartSim(cells, rows, columns)


grid = []
for row in range(6):
    grid.append([])
    for column in range(8):
        grid[row].append(0)

#pygame.init()

running = True


clock = pygame.time.Clock()

tick_count = 0

step = 0

pause = True

speed = 41

currentCoords = []

screen.fill(GREY)
for row in range(0, rows):
    for column in range(0, columns):
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
#Main pygame loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False  # Exit loop/ close pygame when x is clicked
        key=pygame.key.get_pressed()  #checking pressed keys
        if key[pygame.K_RETURN]:
            if randomize:
                module.StartRandom(cells, rows, columns)
            else:
                module.StartSim(cells, rows, columns)

        elif key[pygame.K_SPACE]:
            if pause:
                pause = False
            else:
                pygame.display.set_caption('Conways Game of Life - PAUSED')
                pause = True 

        elif event.type == pygame.MOUSEBUTTONDOWN and pause:
            # If Left Click Make wall
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                module.SetWall(cells[column][row])

            # If Right click make End
            elif event.button == 2:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                module.SetEnd(cells[column][row])

            # If Center Click Set Start
            elif event.button == 3:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                module.SetStart(cells[column][row])
            


    
    # Setup Initial Board
    if tick_count % 10 == 0 and pause:
        for row in range(0, rows):
            for column in range(0, columns):
                #if Path
                if cells[column][row].color == 0:
                    color = LIGHT_GREY
                #if Start
                elif cells[column][row].color == 1:
                    color = GREEN
                #if End
                elif cells[column][row].color == 2:
                    color = RED
                #if Wall
                elif cells[column][row].color == 3:
                    color = BLACK    
                #if Current Cell                                                          
                elif cells[column][row].color == 4:
                    color = BLUE 
                else:
                    color = WHITE
                pygame.draw.rect(screen,
                    color,
                    [(MARGIN + WIDTH) * cells[column][row].column + MARGIN,
                    (MARGIN + HEIGHT) * cells[column][row].row + MARGIN,
                    WIDTH, HEIGHT]) 

    # Find Start / End nodes / values
    if tick_count % 2 == 0 and not pause and step == 0:
        startCoords = module.findStart(cells, rows, columns)
        currentCoords.append(startCoords[0])
        currentCoords.append(startCoords[1])
        endCoords = module.findEnd(cells, rows, columns)
        totalDistance = module.findDistance(startCoords, endCoords)
        cells[startCoords[0]][startCoords[1]].gCost = 0
        cells[startCoords[0]][startCoords[1]].hCost = totalDistance
        module.calculateFCost(cells[startCoords[0]][startCoords[1]])
        for row in range(0, rows):
            for column in range(0, columns):
                cells[column][row].hCost = module.findDistance((column, row), endCoords)
        step += 1

    elif tick_count % 1 == 0 and not pause and step < (2 * rows * columns):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    cells[currentCoords[0]+i][currentCoords[1]+j].hCost = module.findDistance((cells[currentCoords[0]+i][currentCoords[1]+j].column, cells[currentCoords[0]+i][currentCoords[1]+j].row), endCoords)                    
                    if i == 0 or j == 0:
                        cells[currentCoords[0]+i][currentCoords[1]+j].gCost = cells[currentCoords[0]][currentCoords[1]].gCost + 10
                    else:
                        cells[currentCoords[0]+i][currentCoords[1]+j].gCost = cells[currentCoords[0]][currentCoords[1]].gCost + 14
                    module.calculateFCost(cells[currentCoords[0]+i][currentCoords[1]+j])
                    # if cells[currentCoords[0]+i][currentCoords[1]+j].hCost >= totalDistance:
                    #     cells[currentCoords[0]+i][currentCoords[1]+j].color = 3
                    # else:
                    #     cells[currentCoords[0]+i][currentCoords[1]+j].color = 0

        screen.fill(GREY)
        for row in range(0, rows):
            for column in range(0, columns):
                #if Path
                if cells[column][row].color == 0:
                    color = LIGHT_GREY
                #if Start
                elif cells[column][row].color == 1:
                    color = GREEN
                #if End
                elif cells[column][row].color == 2:
                    color = RED
                #if wall
                elif cells[column][row].color == 3:
                    color = BLACK       
                #if Current Cell
                elif cells[column][row].color == 4:
                    color = BLUE                                                      
                else:
                    color = WHITE
                pygame.draw.rect(screen,
                    color,
                    [(MARGIN + WIDTH) * cells[column][row].column + MARGIN,
                    (MARGIN + HEIGHT) * cells[column][row].row + MARGIN,
                    WIDTH, HEIGHT]) 

        currentCoordsNew = []
        currentCoordsNew.append(module.ChooseNext(cells, rows, columns,currentCoords)[0])
        currentCoordsNew.append(module.ChooseNext(cells, rows, columns,currentCoords)[1])
        currentCoords = currentCoordsNew
        if cells[currentCoords[0]][currentCoords[1]].color != 1:
            cells[currentCoords[0]][currentCoords[1]].color = 4
        step += 1

        if currentCoords == list(endCoords):
            print('END FOUND')
            step = (2 * rows * columns) + 1
        else:
            print(currentCoords, endCoords)

    tick_count += 1
    clock.tick(60)
   
    pygame.display.flip()