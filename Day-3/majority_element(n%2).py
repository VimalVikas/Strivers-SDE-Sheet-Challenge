def majorityElement(self, nums: List[int]) -> int:
    element = 0
    count = 0

    for num in nums:
        if count == 0:
            element = num
            count = 1
        elif element == num:
            count += 1
        else:
            count -= 1
    return element
            