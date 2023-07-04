def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def dfs(idx,ds,target):
        if idx == len(candidates):
            if target == 0:
                result.append(ds[::])
            return
        if candidates[idx] <= target:
            ds.append(candidates[idx])
            dfs(idx,ds,target-candidates[idx])
            ds.pop()
        dfs(idx+1,ds,target)
    result = []
    dfs(0,[],target)
    return result
        