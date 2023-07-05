def permute(self, nums: List[int]) -> List[List[int]]:
    def dfs(idx):
        if idx == n:
            res.append(nums[::])
            return
        for i in range(idx,n):
            nums[idx],nums[i] = nums[i],nums[idx]
            dfs(idx+1)
            nums[i],nums[idx] = nums[idx],nums[i]

    n = len(nums)
    if n == 0:
        return []
    res = []
    dfs(0)
    return res