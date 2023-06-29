def nextPermutation(self, nums: List[int]) -> None:
    n = len(nums)
    pointer = n-2
    if n <= 2:
        return nums.reverse()
    while pointer >=0 and nums[pointer] >= nums[pointer+1]:
        pointer -= 1
    
    if pointer == -1:
        return nums.reverse()
    
    for i in range(n-1,pointer,-1):
        if nums[i] > nums[pointer]:
            nums[i],nums[pointer] = nums[pointer],nums[i]
            break
    nums[pointer+1:] = reversed(nums[pointer+1:])
    return nums