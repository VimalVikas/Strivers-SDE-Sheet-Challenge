def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root!=None and root.val!=val:
        if root.val > val:
            root=root.left
        else:
            root=root.right
    return root