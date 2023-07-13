def repeatedStringMatch(self, a: str, b: str) -> int:
    if b in a:
        return 1
    m,n=1,len(b)
    copy=a
    while b!=copy and len(copy)<=n:
        m+=1
        copy=a*m
    if b in copy:
        return m
    if b in a*(m+1):
        return m+1
    return -1