"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
YouTube: https://www.youtube.com/channel/UCn2KHtlnvJNd3oRqH7tMjkg
email: emailtomohitsingh@gmail.com
Instagram: @mohit_was_here
"""
def nextSpace(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r,c)
    return -1

def check(board,row,col,num):
    for x in range(9):
        if board[row][x]==num:
            return False
        if board[x][col]==num:
            return False
    ro=row//3*3
    co=col//3*3
    for r in range(ro,ro+3):
        for c in range(co,co+3):
            if board[r][c]==num and (row,col)!=(r,c):
                return False
    return True

def printBoard(board):
    horLine = '-'*22
    for num in range(9):
        if num%3==0 and num!=0:
            print(horLine)
        row = list(map(str, board[num]))
        print(' '.join(row[0:3])+' | '+' '.join(row[3:6])+' | '+' '.join(row[6:]))

def recuSolve(board):
    space = nextSpace(board)
    if space == -1:
        return True
    row, col = space
    for x in range(9):
        if check(board, row, col, x+1):
            board[row][col]=x+1
            if recuSolve(board):
                return True
    board[row][col]=0
    return False

while True:
    print('Enter a file name of a sudoku file. Files should use 0s as blank spaces')
    print('There are five preset files availible to use, ex: grid1.txt or grid5.txt\nEnter 0 to stop.')
    file = input()

    if file == 0:
        break

    grid = []
    with open(file,'r') as file:
        for line in file:
            grid.append(list(map(int,line.strip())))

    if recuSolve(grid):
        printBoard(grid)
        break
    else:
        print('File was formatted incorrectly or is unsolveable.\n')

