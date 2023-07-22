def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(row,col):
        vis[row][col] = '1'
        dirc = [[0,-1],[0,1],[-1,0],[1,0]]

        for dr,dc in dirc:
            nrow, ncol = dr+row, dc+col
            if nrow in range(n) and ncol in range(m) and not vis[nrow][ncol] and grid[nrow][ncol] == "1":
                dfs(nrow, ncol)
        return
    
    n,m = len(grid),len(grid[0])
    vis = [[0]*m for i in range(n)]
    islands = 0
    for row in range(n):
        for col in range(m):
            if not vis[row][col] and grid[row][col] == '1':
                dfs(row, col)
                islands += 1
    return islands