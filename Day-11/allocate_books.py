def isPossible(n,m,mid):
    dayCount = 1
    timeCount = 0
    for i in range(m):
        if timeCount + time[i] <= mid:
            timeCount += time[i]
        else:
            dayCount += 1
            if dayCount > n or time[i] > mid:
                return False
            timeCount = time[i]
    return True
start = 0
end = sum(time)
ans = -1
while start <= end:
    mid = int(start + (end-start)/2)
    if isPossible(n,m,mid):
        ans = mid
        end = mid-1
    else:
        start = mid + 1
return ans