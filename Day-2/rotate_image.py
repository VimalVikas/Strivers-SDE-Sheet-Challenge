def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    for row in range(rows):
        for col in range(row):
            matrix[row][col],matrix[col][row] = matrix[col][row], matrix[row][col]
    
    for row in range(rows):
        matrix[row].reverse()
    
    return matrix