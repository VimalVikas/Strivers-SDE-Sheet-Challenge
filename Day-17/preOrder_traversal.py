def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def preorder(root):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
        return
    res = []
    preorder(root)
    return res