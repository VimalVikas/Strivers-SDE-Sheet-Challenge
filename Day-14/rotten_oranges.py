def orangesRotting(self, grid: List[List[int]]) -> int:
    n,m = len(grid),len(grid[0])
    q = []
    tm = 0
    count = frsOrange = 0
    vis = [[0]*m for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if grid[row][col] == 2:
                q.append([row,col,0])
                vis[row][col] = 2
            if grid[row][col] == 1:
                frsOrange += 1
    dirc = [[0,-1], [0,1], [-1,0], [1,0]]
    while q:
        row,col,t = q.pop(0)
        tm = max(t,tm)
        for dr,dc in dirc:
            nrow = dr + row
            ncol = dc + col
            if nrow in range(n) and ncol in range(m) and grid[nrow][ncol] == 1 and not vis[nrow][ncol]:
                q.append([nrow,ncol,tm+1])
                vis[nrow][ncol] = 2
                count += 1

    if count != frsOrange:
        return -1
    return tm