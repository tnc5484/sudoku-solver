import cell

cell = cell.cell
print("hello world")

size = 9

#initialize an empty sudoko board
def initBoard():
    puzzle = []
    for x in range(size):
        puzzle.append([])
        for y in range(size):
            puzzle[x].append(cell(0))
    return puzzle

#prints a sudoku board
def printBoard(board):
    for i, row in enumerate(board):
        if i % 3 == 0:
            print("______________________")
        for j, col in enumerate(row):
            if j % 3 == 0:
                print("|", end='')
            print(col.value, end=' ')
        print("|")
    print("______________________")
    return

def loadValue(x, y, val, board):
    board[y][x].value = val

def findInRow(rnum, target, board):
    for col in board[rnum]:
        if col.value == target:
            return True
    return False

def removeFrompotentialInRow(rnum, value, board):
    for colnum, col in enumerate(board[rnum]):
        while value in col.potential:
            col.potential.remove(value)
        if len(col.potential) == 1:
            fillInValue(rnum, colnum, col.potential[0], board)

def findInCol(cnum, target, board):
    for i, row in enumerate(board):
        if board[i][cnum].value == target:
            return True
    return False

def removeFromPotentialInCol(cnum, value, board):
    for rownum, row in enumerate(board):
        while value in board[rownum][cnum].potential:
            board[rownum][cnum].potential.remove(value)
        if len(board[rownum][cnum].potential) == 1:
            fillInValue(rownum, cnum, board[rownum][cnum].potential[0], board)

def findInSquare(x,y,target,board):
    intDivX = x//3
    intDivY = y//3

    minX = 3*intDivX
    minY = 3*intDivY
    maxX = 3*(intDivX+1)
    maxY = 3*(intDivY+1)

    for i in range(minX,maxX):
        for j in range(minY,maxY):
            if board[i][j].value == target:
                return True
    return False

def removeFromPotentialInSquare(x, y, value, board):
    intDivX = x//3
    intDivY = y//3

    minX = 3*intDivX
    minY = 3*intDivY
    maxX = 3*(intDivX+1)
    maxY = 3*(intDivY+1)

    for i in range(minX,maxX):
        for j in range(minY,maxY):
            while value in board[i][j].potential:
                board[i][j].potential.remove(value)
            if len(board[i][j].potential) == 1:
                fillInValue(i, j, board[i][j].potential[0], board)

def checkPossibilities(x, y, board):
    if not (board[x][y].value == 0):
        return
    for val in range(1, size+1):
        if not (findInRow(x, val, board) or findInCol(y, val, board) or findInSquare(x, y, val, board)):
            board[x][y].potential.append(val)
            print("Adding value to potential")
            print(x)
            print(y)
            print(val)
    if len(board[x][y].potential) == 1:
        fillInValue(x, y, board[x][y].potential[0], board)

def fillInValue(x, y, value, board):
    removeFrompotentialInRow(x, value, board)
    removeFromPotentialInCol(y, value, board)
    removeFromPotentialInSquare(x, y, value, board)

    #remove all potential
    board[x][y].potential = []

    board[x][y].value = value


def solve(board):
    complete = False
    for x in range(0,size):
        for y in range(0,size):
            checkPossibilities(x, y, board)
    printBoard(board)

#loads a sudoku puzzle and prints the board
puzzle = initBoard()
loadValue(0,0,2,puzzle)
loadValue(0,5,9,puzzle)
loadValue(1,1,1,puzzle)
loadValue(1,5,8,puzzle)
loadValue(1,7,7,puzzle)
loadValue(1,8,9,puzzle)
loadValue(2,0,9,puzzle)
loadValue(2,2,4,puzzle)
loadValue(2,6,2,puzzle)
loadValue(3,1,4,puzzle)
loadValue(3,4,5,puzzle)
loadValue(3,5,3,puzzle)
loadValue(3,6,6,puzzle)
loadValue(3,7,9,puzzle)
loadValue(4,1,6,puzzle)
loadValue(4,4,7,puzzle)
loadValue(4,7,8,puzzle)
loadValue(5,1,3,puzzle)
loadValue(5,2,5,puzzle)
loadValue(5,3,8,puzzle)
loadValue(5,4,9,puzzle)
loadValue(5,7,4,puzzle)
loadValue(6,2,7,puzzle)
loadValue(6,6,4,puzzle)
loadValue(6,8,8,puzzle)
loadValue(7,0,6,puzzle)
loadValue(7,1,2,puzzle)
loadValue(7,3,3,puzzle)
loadValue(7,7,5,puzzle)
loadValue(8,3,9,puzzle)
loadValue(8,8,6,puzzle)
printBoard(puzzle)
solve(puzzle)
print(len(puzzle[0][1].potential))
print(puzzle[0][1].potential)
