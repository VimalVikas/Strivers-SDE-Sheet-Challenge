def canPartition(self, nums: List[int]) -> bool:
    def recur(idx,target):
        if idx == 0:
            return nums[0] == target
        if target == 0:
            return True
        if target < 0:
            return False
        if dp[idx][target] != -1:
            return dp[idx][target]
        pick = recur(idx-1,target-nums[idx])
        not_pick = recur(idx-1,target)
        dp[idx][target] = pick or not_pick
        return dp[idx][target]
    totsum = sum(nums)
    if totsum % 2:
        return False
    
    dp = [[-1]*(totsum//2+1) for _ in range(len(nums))]
    
    return recur(len(nums)-1,totsum//2)