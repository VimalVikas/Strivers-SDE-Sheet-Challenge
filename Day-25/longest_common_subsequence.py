def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    n,m =len(text1), len(text2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0
    
    for idx1 in range(1,n+1):
        for idx2 in range(1,m+1):
            if text1[idx1-1] == text2[idx2-1]:
                dp[idx1][idx2] = 1 + dp[idx1-1][idx2-1]
            else:
                dp[idx1][idx2] = max(dp[idx1-1][idx2],dp[idx1][idx2-1])
            
    return dp[n][m]