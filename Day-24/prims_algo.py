def spanningTree(self, V, adj):
    pq = []
    vis = [0]*V
    heapq.heappush(pq,[0,0])
    sums = 0
    
    while pq:
        wt,node = heapq.heappop(pq)
        if vis[node]:
            continue
        vis[node] = 1
        sums += wt
        
        for adjNode, edwt in adj[node]:
            heapq.heappush(pq,[edwt, adjNode])
    return sums