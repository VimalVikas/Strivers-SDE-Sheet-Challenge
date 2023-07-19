def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def BST(nums, start, end):
        if start >= end: return None
        return TreeNode(
            val = nums[(start+end)//2],
            left = BST(nums,start, (start+end)//2),
            right = BST(nums, 1+(start+end)//2, end)
        )
    return BST(nums, 0, len(nums))