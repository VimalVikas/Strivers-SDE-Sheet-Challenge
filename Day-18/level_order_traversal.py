def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    ans = []
    q = [root]

    while q:
        temp = []
        for i in range(len(q)):
            node = q.pop(0)
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(temp)
    return ans