def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    cur_count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            cur_count += 1
        else:
            cur_count = 0
        max_count = max(max_count, cur_count)
    return max_count
    
    