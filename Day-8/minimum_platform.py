def minimumPlatform(self,n,arr,dep):
    # code here
    
    arr.sort()
    dep.sort()
    
    max_platform = 1
    cur_platform = 1
    
    i = 1
    j = 0
    
    while i < n and j < n:
        if arr[i] <= dep[j]:
            cur_platform += 1
            i += 1
        else:
            cur_platform -= 1
            j += 1
        max_platform = max(max_platform, cur_platform)
    return max_platform