def bellman_ford(self, V, edges, S):
    #code here
    dist = [100000000]*V
    dist[S] = 0
    
    for i in range(V):
        for u,v,wt in edges:
            if dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
    
    for u,v,wt in edges:
        if dist[u]+wt < dist[v]:
            dist[v] = dist[u] + wt
            return [-1]
    return dist