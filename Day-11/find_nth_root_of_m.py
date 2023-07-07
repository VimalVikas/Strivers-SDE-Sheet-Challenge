def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    start = 2
    end = m-1

    while start <= end:
        mid = (end - start)//2
        if mid**n == m:
            return mid
        elif mid**n < m:
            start = mid + 1
        else:
            end = mid -1
    return -1
