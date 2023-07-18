def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    q = [root]
    ans = []
    flag = 0

    while q:
        temp = []
        for i in range(len(q)):
            node = q.pop(0)
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if flag:
            temp = temp[::-1]
        flag = not flag
        ans.append(temp[::])
    return ans