def findMedian(self, A):
    def count_smaller_than_equal_to_mid(row, mid):
        low = 0
        high = len(row) - 1
        while low <= high:
            md = (low + high) >> 1
            if row[md] <= mid:
                low = md + 1
            else:
                high = md - 1
        return low

    low = 1
    high = int(1e9)
    n = len(A)
    m = len(A[0])
    while low <= high:
        mid = (low + high) >> 1
        cnt = 0
        for i in range(n):
            cnt += count_smaller_than_equal_to_mid(A[i], mid)
        if cnt <= (n * m) // 2:
            low = mid + 1
        else:
            high = mid - 1
    return low