def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = []

    if n < 3:
        return ans

    for idx1 in range(0,n-3):
        if idx1 > 0 and nums[idx1] == nums[idx1-1]:
            continue
        for idx2 in range(idx1+1, n-2):
            if idx2 > idx1+1 and nums[idx2] == nums[idx2-1]:
                continue
            
            idx3 = idx2 + 1
            idx4 = n-1
            while idx3 < idx4:
                sums = nums[idx1] + nums[idx2] + nums[idx3] + nums[idx4]
                if sums < target:
                    idx3 += 1
                elif sums > target:
                    idx4 -= 1
                else:
                    ans.append([nums[idx1], nums[idx2], nums[idx3], nums[idx4]])
                    idx3 += 1
                    idx4 -= 1
                    while idx3 < idx4 and nums[idx3] == nums[idx3-1]:
                        idx3 += 1
                    while idx4 > idx3 and nums[idx4] == nums[idx4+1]:
                        idx4 -= 1

    return ans