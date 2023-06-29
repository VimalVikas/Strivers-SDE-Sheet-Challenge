def maxProfit(self, prices: List[int]) -> int:
    maxi = -1e9
    mini = prices[0]

    for price in prices:
        mini = min(mini, price)
        maxi = max(maxi, price - mini)
    return maxi