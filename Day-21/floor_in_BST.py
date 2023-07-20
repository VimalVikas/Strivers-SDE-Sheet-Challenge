def ansInBST(root, X):
    ans = -1
    while root:
        if root.data == X:
            ans = root.data
            return ans
        if root.data < X:
            ans= root.data
            root = root.right
        else:
            root = root.left
    return ans