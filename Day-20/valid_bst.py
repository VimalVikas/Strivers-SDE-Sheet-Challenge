def isValidBST(self, root):
    def isBST(min_range, max_range,cur):
        if not cur:
            return True
        if cur.val <= min_range or cur.val >= max_range:
            return False
        return isBST(min_range, cur.val,cur.left) and isBST(cur.val, max_range, cur.right)
    min_range = float("-inf")
    max_range = float("inf")
    return isBST(min_range,max_range,root)