def topView(self,root):
    
    # code here
    ans = []
    if root is None:
        return ans

    mpp = {}
    q = [(root, 0)]
    while q:
        node, line = q.pop(0)
        if line not in mpp:
            mpp[line] = node.data

        if node.left:
            q.append((node.left, line - 1))
        if node.right:
            q.append((node.right, line + 1))

    for line in sorted(mpp.keys()):
        ans.append(mpp[line])

    return ans