def lengthOfLongestSubstring(self, s: str) -> int:
    index_counter = {}
    length = left = right = 0
    while right < len(s):
        if s[right] not in index_counter:
            index_counter[s[right]] = right
        else:
            left = max(left, index_counter[s[right]]+1)
            index_counter[s[right]] = right
        right += 1
        length = max(length, right - left)
    return length
    