def isPossible(a, n, cows, minDist) -> bool:
    cntCows = 1
    lastPlacedCow = a[0]
    for i in range(1, n):
        if a[i] - lastPlacedCow >= minDist:
            cntCows += 1
            lastPlacedCow = a[i]
    if cntCows >= cows:
        return True
    return False

def aggressiveCows(stalls, cows):
    # Write your code here.
    stalls.sort()
    n = len(stalls)
    low = 1
    high = stalls[n - 1] - stalls[0]
    while low <= high:
        mid = (low + high) >> 1
        if isPossible(stalls, n, cows, mid):
            low = mid + 1
        else:
            high = mid - 1
    return high

