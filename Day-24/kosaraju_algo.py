def max_num_of_substrings(self, s: str) -> List[str]:
    # some nasty pre-compute in order to build the graph in O(N) time
    mins = [float('inf')] * 26
    maxs = [-1] * 26
    exists = [False] * 26
    prefix_sum = [[0] * 26 for _ in range(len(s) + 1)]
    
    for i in range(len(s)):
        for j in range(26):
            prefix_sum[i + 1][j] = prefix_sum[i][j]
        c_idx = ord(s[i]) - ord('a')
        prefix_sum[i + 1][c_idx] += 1
        mins[c_idx] = min(mins[c_idx], i)
        maxs[c_idx] = max(maxs[c_idx], i)
        exists[c_idx] = True

    # build graph, using adjacency matrix
    graph = [[False] * 26 for _ in range(26)]
    for i in range(26):
        if exists[i]:
            for j in range(26):
                if prefix_sum[maxs[i] + 1][j] - prefix_sum[mins[i]][j] > 0:
                    graph[i][j] = True

    # kosaraju algorithm to find scc
    stack = []
    visited = [False] * 26
    for i in range(26):
        if exists[i] and not visited[i]:
            self.dfs(i, graph, stack, visited)

    batch = 0  # 'id' of each SCC
    batches = [-1] * 26
    degree = [0] * 26  # out-degree of each SCC
    while stack:
        v = stack.pop()
        if batches[v] < 0:
            self.dfs(v, graph, batches, batch, degree)
            batch += 1

    res = []
    for i in range(batch - 1, -1, -1):
        if degree[i] == 0:
            _min = float('inf')
            _max = -1
            for j in range(26):
                if batches[j] == i:
                    _min = min(mins[j], _min)
                    _max = max(maxs[j], _max)
            res.append(s[_min: _max + 1])

    return res

def dfs(self, v, graph, stack, visited):
    if not visited[v]:
        visited[v] = True
        for i in range(26):
            if graph[v][i] and not visited[i]:
                self.dfs(i, graph, stack, visited)
        stack.append(v)

def dfs(self, v, graph, batches, batch, degree):
    if batches[v] < 0:
        batches[v] = batch
        for i in range(26):
            if graph[i][v]:
                self.dfs(i, graph, batches, batch, degree)
    else:
        if batches[v] != batch:
            degree[batches[v]] += 1
