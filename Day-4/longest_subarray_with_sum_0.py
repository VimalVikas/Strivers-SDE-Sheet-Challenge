def maxLen(self, n, arr):
    #Code here
    store = {}
    cur_sum = 0
    maxi = 0
    
    for i in range(n):
        cur_sum += arr[i]
        if cur_sum == 0:
            maxi = max(maxi, i+1)
        elif cur_sum in store:
            maxi = max(maxi, i-store[cur_sum])
        else:
            store[cur_sum] = i
    return maxi
