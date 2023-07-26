def minCost(self, n: int, cuts: List[int]) -> int:
    def recur(i,j):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        mini = 1e9
        for ind in range(i,j+1):
            cost = cuts[j+1] - cuts[i-1] + recur(i,ind-1) + recur(ind+1,j)
            mini = min(mini,cost)
        dp[i][j] = mini
        return dp[i][j]

    c=len(cuts)
    dp=[[-1 for _ in range(c+1)]for _ in range(c+1)]
    cuts.append(n)
    cuts.insert(0,0)
    cuts.sort()
    return recur(1,c)