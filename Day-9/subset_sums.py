def subsetSums(self, arr, N):
    # code here
    def subsets(idx,sums):
        #  base condition
        if idx == len(arr):
            ans.append(sums)
            return
        #  recursive calling to take element in sum
        subsets(idx+1, sums + arr[idx])
        
        #  recursive calling to not to take element in sum
        subsets(idx+1, sums)
        
    ans = []
    subsets(0,0)
    return ans