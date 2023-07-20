def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    def small(root):
        if not root:
            return 0
        small(root.left)
        count[0] += 1
        if count[0] == k:
            final[0] = root.val
        small(root.right)
    count = [0]
    final = [0]
    small(root)
    return final[0]