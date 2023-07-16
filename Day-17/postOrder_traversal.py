def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.right)
        res.append(root.val)
        return
    res = []
    postorder(root)
    return res