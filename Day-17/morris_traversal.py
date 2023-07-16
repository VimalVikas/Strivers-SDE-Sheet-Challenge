def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    inorder = []
    cur = root

    while cur:
        if cur.left is None:
            inorder.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right is not None and prev.right != cur:
                prev = prev.right

            if prev.right is None:
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                inorder.append(cur.val)
                cur = cur.right

    return inorder