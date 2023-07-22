def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
    # code here
    q = [0]
    vis = [0] * V
    vis[0] = 1
    ans = []
    
    while q:
        node = q.pop(0)
        ans.append(node)
        for adjNode in adj[node]:
            if not vis[adjNode]:
                q.append(adjNode)
                vis[adjNode] = 1
    return ans