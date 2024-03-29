def countAndSay(self, n: int) -> str:
    res = []
    
    for _ in range(n):
        if not res: res = ['1']
        else:
            newRes = []
            i = 0
            
            while i < len(res):
                count = 0
                curr = res[i]
                
                while i < len(res) and res[i] == curr: # loop until digits are same.
                    count += 1
                    i += 1
                
                newRes += [str(count), curr]
            
            res = newRes
    
    return ''.join(res)