def solve(self,board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
    
                for c in range(1,10):
                    if self.isValid(board,i,j,c):
                        board[i][j] = str(c)
                    
                        if self.solve(board):
                            return True
                        else:
                            board[i][j] = '.'

                return  False
    return True

def isValid(self,board,row,col,c):
    for i in range(len(board)):
        if board[row][i] == str(c):
            return False
        if board[i][col] == str(c):
            return False
        if board[3*(row//3)+(i//3)][3*(col//3)+i%3] == str(c):
            return False
    return True
def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    self.solve(board)