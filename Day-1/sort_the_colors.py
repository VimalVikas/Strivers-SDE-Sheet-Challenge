def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = run = 0
    j = len(nums)-1

    while run <= j:
        if nums[run] == 0:
            nums[i],nums[run] = nums[run], nums[i]
            i += 1
            run += 1
        elif nums[run] == 1:
            run += 1
        else:
            nums[run], nums[j] = nums[j], nums[run]
            j -= 1
    return nums
    