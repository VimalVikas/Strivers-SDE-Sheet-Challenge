def prevSmaller(self, A):
    st = [-1]
    ans = []
    for i in A:
        while st and st[-1] >= i:
            st.pop()
        ans.append(st[-1])
        st.append(i)
    return ans