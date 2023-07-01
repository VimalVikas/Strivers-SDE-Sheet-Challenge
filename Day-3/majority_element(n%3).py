def majorityElement(self, nums: List[int]) -> List[int]:
    n = len(nums)
    num1 = -1
    num2 = -2
    c1 = c2 = 0
    for num in nums:
        if num == num1:
            c1 += 1
        elif num == num2:
            c2 += 1
        elif c1 == 0:
            num1 = num
            c1 = 1
        elif c2 ==0:
            num2 = num
            c2 += 1
        else:
            c1 -= 1
            c2 -= 1
    count1 = 0
    count2 = 0

    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1
    ans = []
    if count1 > n/3:
        ans.append(num1)
    if count2 > n/3:
        ans.append(num2)
    return ans
