def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def recur(i):
        if i in dp:
            return dp[i]
        j = i-1
        while j >= 0:
            if s[j:i] in word_set and recur(j):
                dp[i] = True
                return dp[i]
            j -= 1
        dp[i] = False
        return dp[i]
        
    word_set = set(wordDict)
    dp = {0: True}
    return recur(len(s))