def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def tree(preorder,preStart,preEnd):
        if preStart > preEnd or not len(preorder):
            return None
        root = TreeNode(preorder.pop(0))
        root.left = tree(preorder,preStart, inorderMap[root.val]-1)
        root.right = tree(preorder,inorderMap[root.val]+1, preEnd)
        return root
    inorderMap = {inorder[i] : i for i in range(len(inorder)) }
    build_tree = tree(preorder,0,len(preorder)-1)
    return build_tree