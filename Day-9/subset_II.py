def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    def dfs(idx, ds):
        res.append(ds[::])
        for i in range(idx,n):
            if i > idx and nums[i] == nums[i-1]:
                continue
            ds.append(nums[i])
            dfs(i+1,ds)
            ds.pop()
    
    n = len(nums)
    if not n:
        return []
    res = []
    dfs(0,[])
    return res
