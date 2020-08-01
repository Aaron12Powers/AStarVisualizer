import random
import math

'''
WHITE = 5
LIGHT_GREY = 0
GREY = (128, 128, 128)
BLACK = 3
GREEN = 1
RED = 2
BLUE = 4
'''


class Cell(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.color = 5
        self.isStart = 0
        self.isEnd = 0
        self.isWall = 0
        self.isPath = 0
        self.gCost = 9999
        self.hCost = 9999
        self.fCost = 9999

#setup first cell of simulation
def StartSim(cells, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            cells[column][row].color = 5


def StartRandom(cells, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            randomRoll = random.randint(0,100)
            if randomRoll % 5 == 0:
                cells[column][row].color = 1
            else:
                cells[column][row].color = 0

def StartBlank(cells, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            cells[column][row].color = 0


def RunSim(oldCells, newCells, rows, columns):
    print('runsim')

def SetPath(cell):
    cell.isWall = True
    cell.isStart = False
    cell.isEnd = False
    cell.isWall = False
    cell.color = 0

def SetStart(cell):
    cell.isWall = False
    cell.isStart = True
    cell.isEnd = False
    cell.isWall = False
    cell.color = 1

def SetEnd(cell):
    cell.isWall = True
    cell.isStart = False
    cell.isEnd = True
    cell.isWall = False
    cell.color = 2

def SetWall(cell):
    cell.isStart = False
    cell.isEnd = False
    if cell.isWall == False:
        cell.isWall = True
        cell.color = 3
    else:
        cell.isWall = False
        cell.color = 5
    

def findStart(cells, rows, columns):
    for row in range(rows):
        for column in range(columns):
            if cells[column][row].isStart:
                return (cells[column][row].column, cells[column][row].row)

def findEnd(cells, rows, columns):
    for row in range(rows):
        for column in range(columns):
            if cells[column][row].isEnd:
                return (cells[column][row].column, cells[column][row].row)

def findDistance(start, end):
    column = abs(start[0] - end[0])
    row = abs(start[1] - end[1])
    return int(math.sqrt((row * row) + (column * column)) * 10)


def calculateFCost(cell):
    cell.fCost = cell.hCost + cell.gCost

def ChooseNext(cells, rows, columns, currentCoords):
    currentLow = 999999
    currentLowCell = [1, 1]
    for row in range(rows):
        for column in range(columns):
            if cells[column][row].isWall: 
                continue
            if cells[column][row].color == 4 or cells[column][row].color == 1:
                continue
            for i in range(rows):
                for j in range(columns):
                    if cells[j][i].color == 4 or cells[j][i].color == 1:
                        if findDistance((j, i), (column, row)) <= 14 and findDistance((j, i), (column, row)) <= 14:
                            cells[column][row].gCost = findDistance((j, i), (column, row)) + cells[j][i].gCost
                            calculateFCost(cells[column][row])
                            print(cells[column][row].gCost)

            if cells[column][row].fCost < currentLow:
                # print(currentCoords, (column, row))
                if tuple(currentCoords) != (column, row):
                    currentLow = cells[column][row].fCost
                    currentLowCell = []
                    currentLowCell.append(column)
                    currentLowCell.append(row)
    return currentLowCell
        