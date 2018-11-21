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
