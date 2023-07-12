def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    res = []
    wndw = deque()
    for i in range(len(nums)):
        # Remove elements that are not in current wndw
        if wndw and wndw[0] <= i - k:
            wndw.popleft()
        
        #Remove smaller elements from the right side of the wndw
        while wndw and nums[wndw[-1]] < nums[i]:
            wndw.pop()
        
        #Add the current element to the wndw
        wndw.append(i)
        
        #Append the maximum element of the current wndw to the res
        if i >= k - 1:
            res.append(nums[wndw[0]])
    
    return res