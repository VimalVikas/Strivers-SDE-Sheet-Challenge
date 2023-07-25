def maxSumIS(self, Arr, n):
    msis = [0]*n
    for i in range(n):
        msis[i] = Arr[i]
        for j in range(i):
            if Arr[i] > Arr[j] and Arr[i] + msis[j] >= msis[i]:
                msis[i] = Arr[i] + msis[j]
    return max(msis)