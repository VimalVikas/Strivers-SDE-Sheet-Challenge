def detect(self, src, adj, vis):
    vis[src] = 1
    q = deque([(src, -1)])
    while q:
        node, parent = q.popleft()
        for adjacentNode in adj[node]:
            if not vis[adjacentNode]:
                vis[adjacentNode] = 1
                q.append((adjacentNode, node))
            elif parent != adjacentNode:
                return True
    return False

def isCycle(self, V, adj):
    vis = [0] * V
    for i in range(V):
        if not vis[i]:
            if self.detect(i, adj, vis):
                return True
    return False