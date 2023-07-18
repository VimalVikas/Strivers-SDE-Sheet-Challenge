def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    cur = root
    while cur:
        if cur.left:
            run = cur.left
            while run.right: run = run.right
            run.right, cur.right, cur.left = cur.right, cur.left, None
        cur = cur.right