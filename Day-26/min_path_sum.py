def minPathSum(self, grid: List[List[int]]) -> int:
    def recur(row,col):
        if row == 0 and col == 0:
            return grid[0][0]

        if row < 0 or col < 0:
            return 1e9

        if dp[row][col] != -1:
            return dp[row][col]

        left = grid[row][col] + recur(row,col-1)
        up = grid[row][col] + recur(row-1,col)
        dp[row][col] = min(left,up)
        return dp[row][col]
        
    n = len(grid)
    m = len(grid[0])
    dp = [[-1] * m for _ in range(n)]
    return recur(n-1, m-1)