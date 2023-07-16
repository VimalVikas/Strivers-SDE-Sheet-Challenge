def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
        return
    res = []
    inorder(root)
    return res