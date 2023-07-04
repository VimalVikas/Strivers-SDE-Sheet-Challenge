def partition(self, s: str) -> List[List[str]]:
    def dfs(idx,ans):
        if idx == len(s):
            result.append(ans[::])
            return
        for i in range(idx,len(s)):
            word = s[idx:i+1]
            if word == word[::-1]:
                ans.append(word)
                dfs(i+1,ans)
                ans.pop()
                
    result = []
    dfs(0,[])
    return result