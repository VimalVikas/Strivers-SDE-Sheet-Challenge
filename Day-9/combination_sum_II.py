def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def dfs(idx,ds,target):
        if target == 0:
            res.append(ds[::])
            return
        for i in range(idx, n):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] <= target:
                ds.append(candidates[i])
                dfs(i+1, ds,target-candidates[i])
                ds.pop()
    n = len(candidates)
    candidates.sort()
    res = []
    dfs(0, [],target)
    return res