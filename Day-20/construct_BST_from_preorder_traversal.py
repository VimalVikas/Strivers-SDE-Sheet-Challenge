def bstFromPreorder(self, A):
    def Tree(A,limit):
        if not A or A[-1] > limit: return None
        node = TreeNode(A.pop())
        node.left = Tree(A,node.val)
        node.right = Tree(A,limit)
        return node

    return Tree(A[::-1], float('inf'))