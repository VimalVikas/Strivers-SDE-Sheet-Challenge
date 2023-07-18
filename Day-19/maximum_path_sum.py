def pathSum(self,root,sums):
    if not root:
        return 0
    left = max(0,self.pathSum(root.left,sums))
    right = max(0,self.pathSum(root.right,sums))
    sums[0] = max(sums[0],left+right+root.val)
    return max(left,right)+root.val

def maxPathSum(self, root: Optional[TreeNode]) -> int:
    sums = [-1000000]
    self.pathSum(root,sums)
    return sums[0]