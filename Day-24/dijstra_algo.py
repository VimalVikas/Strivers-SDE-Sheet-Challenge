def dijkstra(self, V, adj, S):
    pq = []
    dist = [sys.maxsize]*V
    dist[S] = 0
    heapq.heappush(pq,(S,0))
    
    while pq:
        node = heapq.heappop(pq)
        for i in adj[node[0]]:
            if i[1] + dist[node[0]] < dist[i[0]]:
                dist[i[0]] = dist[node[0]] + i[1]
                heapq.heappush(pq,(i[0], [1]))
    return dist