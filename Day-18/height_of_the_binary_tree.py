def maxDepth(self, root: Optional[TreeNode]) -> int:
    def depth(root):
        if not root:
            return 0
        return max(depth(root.left), depth(root.right)) + 1
    return depth(root)