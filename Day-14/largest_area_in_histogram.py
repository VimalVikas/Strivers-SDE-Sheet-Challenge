def largestRectangleArea(self, heights: List[int]) -> int:
    stack = [-1]
    
    ans = 0
    for i in range(len(heights)):
        while(stack[-1] != -1 and heights[i] <= heights[stack[-1]]):
            height = heights[stack.pop()]
            ans = max(ans, height * (i - stack[-1]-1))
        stack.append(i)
    while stack[-1] != -1:
        height = heights[stack.pop()]
        ans = max(ans, height * (len(heights) - stack[-1]-1))
    return ans