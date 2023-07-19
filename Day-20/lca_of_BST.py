    def lca(root, p, q):
        if not root:
            return
        curr = root.val
        if curr > p.val and curr> q.val:
            return lca(root.left, p,q)
        if curr < p.val and curr < q.val:
            return lca(root.right,p,q)
        return root
    if p.val > q.val:
        p,q = q,p
    ans = lca(root,p,q)
    return ans