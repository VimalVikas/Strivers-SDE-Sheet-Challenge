def shortest_distance(self, matrix):
    #Code here
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 1e9
            if i == j:
                matrix[i][j] = 0
    
    for via in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][via]+matrix[via][j])
    
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1e9:
                matrix[i][j] = -1
                
    return matrix