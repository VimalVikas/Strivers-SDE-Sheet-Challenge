def topoSort(self, V, adj):
    # Code here
    q = []
    st = []
    indegree = [0]*V
    
    for i in range(V):
        for node in adj[i]:
            indegree[node] += 1
    
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        node = q.pop(0)
        
        for adjNode in adj[node]:
            indegree[adjNode] -= 1
            if indegree[adjNode] == 0:
                q.append(adjNode)
        st.append(node)
    return st