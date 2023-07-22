def dfs(self, node, parent, vis, adj):
    vis[node] = 1
    for adjacentNode in adj[node]:
        if not vis[adjacentNode]:
            if self.dfs(adjacentNode, node, vis, adj):
                return True
        elif adjacentNode != parent:
            return True
    return False

def isCycle(self, V, adj):
    vis = [0] * V
    for i in range(V):
        if not vis[i]:
            if self.dfs(i, -1, vis, adj):
                return True
    return False




