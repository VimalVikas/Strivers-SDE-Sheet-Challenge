def coinChange(self, coins: List[int], amount: int) -> int:
    def recur(idx,amt):
        if idx == 0:
            if amt % coins[0] == 0:
                return amt//coins[0]
            return 1e9

        if dp[idx][amt] != -1:
            return dp[idx][amt]
        not_take = recur(idx-1,amt)
        take = 1e9
        if coins[idx] <= amt:
            take = 1 + recur(idx,amt-coins[idx])
        dp[idx][amt] = min(take,not_take)
        return dp[idx][amt] 

    n = len(coins)
    dp = [[-1]*(amount + 1)  for _ in range(n)]
    if recur(n-1, amount) >= 1e9:
        return -1
    return recur(n-1, amount)