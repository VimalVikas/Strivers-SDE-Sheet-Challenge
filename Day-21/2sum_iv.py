def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    def solve(root):
        if not root: return
        if k-root.val in hash_map:
            return True
        hash_map[root.val] = True
        return solve(root.right) or solve(root.left)
    hash_map = {}
return solve(root)