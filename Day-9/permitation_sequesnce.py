def getPermutation(self, n: int, k: int) -> str:
    num = []
    fact = 1
    for i in range(1,n):
        fact *= i
        num.append(i)
    num.append(n)
    k = k-1 
    ans = ""
    while True:
        ans = ans + str(num.pop(int(k/fact)))
        if len(num) == 0:
            break
        k = k%fact
        fact = fact/len(num)
    return ans