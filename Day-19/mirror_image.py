def mirror(self,root):
    # Code here
    if not root:
        return 
    self.mirror(root.left)
    self.mirror(root.right)
    root.left, root.right = root.right, root.left
    return