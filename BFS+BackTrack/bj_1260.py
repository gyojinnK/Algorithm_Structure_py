import collections

n, m, v = map(int, input().split())
graph = collections.defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, visited):
    visited.append(v)
    for adj in sorted(graph[v]):
        if adj not in visited:
            dfs(adj, visited)
    return visited

def bfs(v):
    visited = [v]
    q = collections.deque([v])

    while q:
        cur_v = q.popleft()
        for adj in sorted(graph[cur_v]):
            if adj not in visited:
                visited.append(adj)
                q.append(adj)
    return visited

print(' '.join(str(el) for el in dfs(v, [])))
print(' '.join(str(el) for el in bfs(v)))




