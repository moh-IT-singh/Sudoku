"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
email: emailtomohitsingh@gmail.com
"""
class solve:
    def __init__(self,board):
        self.board=board
    
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

    def recuSolve(self, board):
        space = self.nextSpace(board)
        if space == -1:
            self.printBoard(board)
            return True
        row, col = space
        for x in range(9):
            if self.check(board, row, col, x+1):
                board[row][col]=x+1
                if self.recuSolve(board):
                    return True
        board[row][col]=0
        return False
