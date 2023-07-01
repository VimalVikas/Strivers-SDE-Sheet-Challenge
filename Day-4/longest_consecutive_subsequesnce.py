def longestConsecutive(self, nums: List[int]) -> int:
    Set = set(nums)

    long_streak = cur_streak = 0

    for num in nums:
        if num-1 not in Set:
            cur_num = num
            cur_streak = 0
            while cur_num in Set:
                cur_streak += 1
                cur_num += 1
            long_streak = max(long_streak, cur_streak)
    return long_streak