def findPreSuc(self, root, pre, suc, key):
    if node is None:
        return pre, suc
    if s > node.key - key and node.key - key > 0:
        s = node.key - key
        suc = node
        
    elif p > key - node.key and key - node.key > 0:
        p = key - node.key
        pre = node
        
    pre, suc = helper(node.left, key, p, s, pre, suc)
    pre, suc = helper(node.right, key, p, s, pre, suc)
    
    return pre, suc