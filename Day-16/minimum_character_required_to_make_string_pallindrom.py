def solve(self, A):
    ans = 0
    i, j = 0, len(A) - 1

    while i < j:
        if A[i] != A[j]:
            if i == 0:
                j -= 1
                ans += 1
            else:
                ans += i
                i = 0
        else:
            i += 1
            j -= 1

    return ans