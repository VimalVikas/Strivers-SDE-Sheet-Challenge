def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root: return root
    q = [root]
    while q:
        rNode = None
        for i in range(len(q)):
            node = q.pop(0)
            node.next, rNode = rNode, node
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
    return root