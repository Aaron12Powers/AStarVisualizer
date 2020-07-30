
'''
Colors... 
White = 0
Black = 1
Grey = 2
'''
class Cell(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.color = 2

#setup first cell of simulation
def StartSim(cells,rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            if cells[column][row].column != (columns // 2):
                cells[column][row].color = 0
            elif cells[column][row].row != 0:
                cells[column][row].color = 0    
            else:
                cells[column][row].color = 1

def RunSim(cells, rows, columns, rule):
    for row in range(1, rows):
        for column in range(0, columns):
            ruleNumber = rule
            if ruleNumber >= 128:
                ruleNumber = ruleNumber - 128
                if RuleEight(cells, row, column):
                    cells[column][row].color = 1
                    continue
            if ruleNumber >= 64:
                ruleNumber = ruleNumber - 64
                if RuleSeven(cells, row, column):
                    cells[column][row].color = 1
                    continue
            if ruleNumber >= 32:
                ruleNumber = ruleNumber - 32
                if RuleSix(cells, row, column):
                    cells[column][row].color = 1
                    continue
            if ruleNumber >= 16:
                ruleNumber = ruleNumber - 16
                if RuleFive(cells, row, column):
                    cells[column][row].color = 1
                    continue
            if ruleNumber >= 8:
                ruleNumber = ruleNumber - 8
                if RuleFour(cells, row, column):
                    cells[column][row].color = 1
                    continue
            if ruleNumber >= 4:
                ruleNumber = ruleNumber - 4
                if RuleThree(cells, row, column):
                    cells[column][row].color = 1
                    continue
            if ruleNumber >= 2:
                ruleNumber = ruleNumber - 2
                if RuleTwo(cells, row, column):
                    cells[column][row].color = 1
                    continue
            if ruleNumber >= 1:
                ruleNumber = ruleNumber - 1
                if RuleOne(cells, row, column):
                    cells[column][row].color = 1
                    continue
            

    print(columns, rows)
    cells[columns - 1][rows-1].color = 2

def RuleOne(cells, row, column):
    print('RuleOne')
    try:
        if cells[column-1][row-1].color == 0 and cells[column][row-1].color == 0 and cells[column+1][row-1].color == 0:
            return True
        else:
            return False
    except:
        return False

def RuleTwo(cells, row, column):
    print('RuleTwo')
    try:
        if cells[column-1][row-1].color == 0 and cells[column][row-1].color == 0 and cells[column+1][row-1].color == 1:
            return True
        else:
            return False
    except:
        return False

def RuleThree(cells, row, column):
    print('RuleThree')
    try:
        if cells[column-1][row-1].color == 0 and cells[column][row-1].color == 1 and cells[column+1][row-1].color == 0:
            return True
        else:
            return False
    except:
        return False

def RuleFour(cells, row, column):
    print('RuleFour')
    try:
        if cells[column-1][row-1].color == 0 and cells[column][row-1].color == 1 and cells[column+1][row-1].color == 1:
            return True
        else:
            return False
    except:
        return False

def RuleFive(cells, row, column):
    print('RuleFive')
    try:
        if cells[column-1][row-1].color == 1 and cells[column][row-1].color == 0 and cells[column+1][row-1].color == 0:
            return True
        else:
            return False
    except:
        return False

def RuleSix(cells, row, column):
    print('RuleSix')
    try:
        if cells[column-1][row-1].color == 1 and cells[column][row-1].color == 0 and cells[column+1][row-1].color == 1:
            return True
        else:
            return False
    except:
        return False

def RuleSeven(cells, row, column):
    try:
        print('RuleSeven')
        if cells[column-1][row-1].color == 1 and cells[column][row-1].color == 1 and cells[column+1][row-1].color == 0:
            return True
        else:
            return False
    except:
        return False

def RuleEight(cells, row, column):
    print('RuleEight')
    try:
        if cells[column-1][row-1].color == 1 and cells[column][row-1].color == 1 and cells[column+1][row-1].color == 1:
            return True
        else:
            return False
    except:
        return False