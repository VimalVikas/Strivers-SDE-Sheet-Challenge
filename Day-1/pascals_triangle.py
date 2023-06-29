def generate(self, numRows: int) -> List[List[int]]:
    res= []
    for i in range(numRows):
        temp = []
        for j in range(i+1):
            if j == i or j == 0:
                temp.append(1)
            else:
                temp.append(res[i-1][j-1]+res[i-1][j])
        res.append(temp)
    return res