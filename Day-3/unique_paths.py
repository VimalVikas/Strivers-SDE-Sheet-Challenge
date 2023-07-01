def uniquePaths(self, m: int, n: int) -> int:
    # -------- recursive ------
    def dfs(row,col):
        if row == m-1 and col == n-1:
            return 1
        if row == m or col == n:
            return 0
        return dfs(row + 1, col) + dfs(row, col + 1)
        
    return dfs(0, 0)

    # -------- DP ------
    def dfs(row,col):
        if row == m-1 and col == n-1:
            return 1
        if row == m or col == n:
            return 0
        if dp[row][col] != -1:
            return dp[row][col]
        dp[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
        return dp[row][col]
        
    dp = [[-1]* n for _ in range(m)]
    return dfs(0, 0)