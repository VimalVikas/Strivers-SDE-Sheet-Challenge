def dNums(self, A, B):
    arr = []
    map = {}
    
    if B > len(A):
        return arr

    j = 0
    for i in range(len(A)):
        if i < B:
            if A[i] in map:
                num = map[A[i]] + 1
                map[A[i]] = num
            else:
                map[A[i]] = 1
        else:
            arr.append(len(map))
            if map[A[j]] > 1:
                num2 = map[A[j]] - 1
                map[A[j]] = num2
                if A[i] in map:
                    num = map[A[i]] + 1
                    map[A[i]] = num
                else:
                    map[A[i]] = 1
                j += 1
            else:
                map.pop(A[j])
                if A[i] in map:
                    num = map[A[i]] + 1
                    map[A[i]] = num
                else:
                    map[A[i]] = 1
                j += 1
    
    arr.append(len(map))
    return arr