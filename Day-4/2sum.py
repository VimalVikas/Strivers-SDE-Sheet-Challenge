def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = {}

    for i in range(len(nums)):
        if target - nums[i] in result:
            return [i, result[target - nums[i]]]
        else:
            result[nums[i]] = i