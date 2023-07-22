def isBipartite(self, graph: List[List[int]]) -> bool:
    def bfs(start,color,graph,n):
        color[start] = 0
        q = [start]

        while q:
            node = q.pop(0)

            for adjNode in graph[node]:
                if color[adjNode] == -1:
                    color[adjNode] = not color[node]
                    q.append(adjNode)
                elif color[adjNode] == color[node]:
                    return False
    n = len(graph)
    color = [-1]*n
    for i in range(n):
        if color[i] == -1:
            if bfs(i,color,graph,n) == False:
                return False
    return True