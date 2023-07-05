
def solveNQueens(self, n: int) -> List[List[str]]:
    def isSafe(row,col,board,n):      
        dupRow = row
        dupCol = col
        
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1
            row -= 1

        row = dupRow
        col = dupCol

        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1

        row = dupRow
        col = dupCol

        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        return True

    
    def solve(col,board,n):
        if col == n:
            temp = []
            for i in board:
                temp.append("".join(i))
            ans.append(temp)
            return
        for i in range(n):
            if isSafe(i, col, board, n):
                board[i][col] = 'Q'
                solve(col + 1, board, n)
                board[i][col] = '.'
    
    ans = []
    board = [["."]*n for i in range(n)]
    solve(0,board,n)
    return ans