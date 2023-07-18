def tree(self,inorderMap,postorder,postStart,postEnd):
    if postStart > postEnd or not len(postorder):
        return None
    root = TreeNode(postorder.pop())
    root.right = self.tree(inorderMap,postorder,inorderMap[root.val]+1,postEnd)
    root.left = self.tree(inorderMap,postorder,postStart,inorderMap[root.val]-1)
    return root
    
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    inorderMap = {inorder[index] : index for index in range(len(inorder))}
    binary_tree = self.tree(inorderMap,postorder,0,len(postorder)-1)
    return binary_tree