def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    small_word = min(strs, key = len)

    for idx in range(len(small_word)):
        char = small_word[idx]
        for word in strs:
            if word[idx] != char:
                return small_word[:idx]
    return small_word
    