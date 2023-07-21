def dfs(self,row,col,initial_color,copy_image,image,color,n,m):
    copy_image[row][col] = color
    dirc = [[0,1],[0,-1],[1,0],[-1,0]]
    for dr,dc in dirc:
        nrow, ncol = row+dr,col+dc
        if nrow in range(n) and ncol in range(m) and copy_image[nrow][ncol] != color and image[nrow][ncol] == initial_color:
            self.dfs(nrow,ncol,initial_color,copy_image,image,color,n,m)
    
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    initial_color = image[sr][sc]
    copy_image = image
    n = len(image)
    m = len(image[0])
    
    self.dfs(sr,sc,initial_color,copy_image,image,color,n,m)
    
    return copy_image