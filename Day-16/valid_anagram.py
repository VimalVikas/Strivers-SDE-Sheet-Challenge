def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    freq_counter = {}

    for char in s:
        if char in freq_counter:
            freq_counter[char] += 1
        else:
            freq_counter[char] = 1
            
    for char in t:
        if char in freq_counter and freq_counter[char] >= 1:
            freq_counter[char] -= 1
        else:
            return False
    return True