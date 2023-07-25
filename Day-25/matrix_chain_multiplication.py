def matrixMultiplication(self, N, arr):
    dp = [[0]*(N) for i in range(N)]
    for i in range(1,N):
        
        dp[i][i]=0
    for i in range(N-1,0,-1):
        for j in range(i+1,N):
            mini = 1e9
            for k in range(i,j):
                steps = arr[i-1]*arr[k]*arr[j] +dp[k+1][j] + dp[i][k]
                mini = min(mini,steps)
                dp[i][j] = mini
        
    
    return dp[1][N-1]