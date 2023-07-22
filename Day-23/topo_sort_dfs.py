def topoSort(self, V, adj):
    # Code here
    def dfs(node):
        vis[node] = 1
        for adjNode in adj[node]:
            if not vis[adjNode]:
                dfs(adjNode)
        st.append(node)
    vis = [0]*V
    st = []
    for i in range(V):
        if not vis[i]:
            dfs(i)
    return st[::-1]
        