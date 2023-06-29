def maxSubArray(self, nums: List[int]) -> int:
    maxi = 0
    cur_sum = 0

    for num in nums:
        cur_sum += num
        maxi = max(maxi, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return maxi
    