def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def symmetric(left,right):
        if not left and not right:
            return left == right
        if not left or not right or left.val != right.val:
            return False
        return symmetric(left.left,right.right) and symmetric(left.right,right.left)
    return root == None or symmetric(root.left,root.right)