def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    greater = {}
    st =[]
    i = len(nums2)

    for num in nums2:
        greater[num] = -1

    for num in nums2:
        while st and st[-1] < num:
            greater[st.pop()] = num
        st.append(num)
    
    return [greater[x] for x in nums1]
