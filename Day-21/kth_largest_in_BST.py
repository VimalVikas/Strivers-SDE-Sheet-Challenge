def kthLargest(self,root, k):
    #your code here
    inorderTree = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        inorderTree.append(root.data)
        inorder(root.right)
    inorder(root)
    return inorderTree[-k]