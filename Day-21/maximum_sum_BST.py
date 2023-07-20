def helper(self, node):
    if not node:
        return NodeValue(float('inf'), float('-inf'), 0)

    left = self.helper(node.left)
    right = self.helper(node.right)

    if left.maxNode < node.val and node.val < right.minNode:
        curSum=left.Sum+ right.Sum + node.val
        self.maxi=max(self.maxi,curSum)
        return NodeValue(min(node.val, left.minNode), max(node.val, right.maxNode),curSum)

    return NodeValue(float('-inf'), float('inf'), max(left.Sum, right.Sum))

def maxSumBST(self, root: Optional[TreeNode]) -> int:
    self.maxi=0
    ans=self.helper(root).Sum 
    return self.maxi