def compareVersion(self, version1: str, version2: str) -> int:
    version1, version2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))  
    for reversion1, reversion2 in zip_longest(version1, version2, fillvalue=0):
        if reversion1 == reversion2:
            continue

        return -1 if reversion1 < reversion2 else 1 

    return 0