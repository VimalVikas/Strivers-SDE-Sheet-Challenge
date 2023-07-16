def LeftView(root):
def leftView(root, level):
    if not root:
        return
    if level == len(res):
        res.append(root.data)
    if root.left:
        leftView(root.left, level+1)
    if root.right:
        leftView(root.right, level+1)
    return
res = []
leftView(root, 0)
return res
    