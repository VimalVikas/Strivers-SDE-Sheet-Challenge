def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    ans = []
    
    for i in range(n-2):
        if i == 0 or i > 0 and nums[i] != nums[i-1]:
            start = i+1
            end = n-1
            
            while start < end:
                sums = nums[i] + nums[start] + nums[end]
                if sums == 0:
                    ans.append([nums[i], nums[start], nums[end]])
                    
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                        
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                        
                    start += 1
                    end -= 1
                    
                elif  sums < 0:
                    start += 1
                    
                else:
                        end -= 1
                        
    return ans