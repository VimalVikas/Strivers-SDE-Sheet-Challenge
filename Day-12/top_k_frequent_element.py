def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq_element = [[] for i in range(len(nums)+1)]
    frequency = {}
    res = []

    for num in nums:
        frequency[num] = 1 + frequency.get(num,0)
    
    for num, count in frequency.items():
        freq_element[count].append(num)

    for idx in range(len(freq_element)-1,0,-1):
        for num in freq_element[idx]:
            res.append(num)
            if len(res)== k:
                return res



    