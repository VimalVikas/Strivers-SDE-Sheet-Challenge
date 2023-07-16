def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    q= collections.deque()
    width = 0
    q.append((0, root))
    while q:
        width = max(width, q[-1][0]-q[0][0] +1)
        for i in range(len(q)):
            idx, node  = q.popleft()
            if node.left:
                q.append((2*idx, node.left))
            if node.right:
                q.append((2*idx+1, node.right))
    return width