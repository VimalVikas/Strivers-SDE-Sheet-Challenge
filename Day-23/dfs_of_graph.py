def dfsOfGraph(self, V, adj):
    # code here
    def dfs(root):
        vis[root] = 1
        res.append(root)
        for adjNode in adj[root]:
            if not vis[adjNode]:
                dfs(adjNode)
    
    vis = [0]*V
    res = []
    dfs(0)
    return res