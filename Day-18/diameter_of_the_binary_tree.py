def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def diameter(root):
        if not root:
            return 0
        left = diameter(root.left)
        right = diameter(root.right)
        self.maxi = max(self.maxi, left+right)
        return max(left,right) + 1
    self.maxi = 0
    diameter(root)
    return self.maxi