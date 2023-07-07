def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    start = 0
    end = n-1

    while start <= end:
        mid = start + (end-start) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[start] <= nums[mid]:
            if nums[start] <= target and nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        else:
            if nums[mid] < target and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return -1
