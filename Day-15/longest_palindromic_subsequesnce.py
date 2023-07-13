def longestPalindrome(self, s: str) -> str:
    n=len(s)
    #for storing the maximum pallindromic substr length
    maxi=0
    start=0
    end=0
    for i in range(n):            
        low=i-1
        high=i
        while low>=0 and high < n and s[low]==s[high]:
            if high-low+1>maxi:
                maxi=high-low+1
                start=low
                end=high
            low-=1
            high+=1
        low=i-1
        high=i+1
        while low>=0 and high < n and s[low]==s[high]:
            if high-low+1>maxi:
                maxi=high-low+1
                start=low
                end=high
            low-=1
            high+=1
    return s[start:end+1]