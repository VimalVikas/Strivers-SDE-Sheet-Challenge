def knapSack(self,W, wt, val, n):
    
    # code here
    def recur(idx,Wt):
        if idx == 0:
            if wt[0] <= Wt:
                return val[0]
            return 0
            
        if dp[idx][Wt] != -1:
            return dp[idx][Wt]
            
        not_take = recur(idx-1,Wt)
        take = -1e9
        if wt[idx] <= Wt:
            take = val[idx] + recur(idx-1,Wt-wt[idx])
            
        dp[idx][Wt] = max(take,not_take)
        return dp[idx][Wt]
    
    dp = [[-1]*(W+1) for _ in range(n)]
    return recur(n-1,W)