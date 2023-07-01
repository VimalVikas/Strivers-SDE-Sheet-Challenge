def solve(self, A, B):
    hashMap = {}
    xor = 0
    count = 0
    for i in range(len(A)):
        xor = xor ^ A[i]
        if xor == B:
            count += 1
        if xor ^ B in hashMap:
            count += hashMap[xor^B]
        if xor in hashMap:
            hashMap[xor] += 1
        else:
            hashMap[xor] = 1
    return count