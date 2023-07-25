def maxProduct(self, nums: List[int]) -> int:
    if not nums: return 0

    dp = [(0,0) for _ in range(len(nums))]
    dp[0] = (nums[0], nums[0])

    for i in range(1,len(nums)):
        maxi = max(nums[i], dp[i-1][0]*nums[i], dp[i-1][1]*nums[i])
        mini = min(nums[i], dp[i-1][0]*nums[i], dp[i-1][1]*nums[i])
        dp[i] = (maxi, mini)
    return max(dp)[0]