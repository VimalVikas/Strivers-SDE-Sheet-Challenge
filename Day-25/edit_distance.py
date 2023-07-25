def minDistance(self, word1: str, word2: str) -> int:
    def recur(i1,i2):
        if i1 < 0:
            return i2+1
        if i2 < 0:
            return i1+1
        if dp[i1][i2] != -1:
            return dp[i1][i2]

        if word1[i1] == word2[i2]:
            dp[i1][i2] = recur(i1-1,i2-1)
            return dp[i1][i2]
        else:
            dp[i1][i2] = 1 + min(recur(i1-1,i2),min(recur(i1-1,i2-1),recur(i1,i2-1)))
            return dp[i1][i2]
    n,m = len(word1),len(word2)
    dp = [[-1]*(m+1) for _ in range(n+1)]
    return recur(n-1,m-1)