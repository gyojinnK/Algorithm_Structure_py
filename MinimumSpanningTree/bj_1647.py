import heapq
from pprint import pprint

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
g = [[] for _ in range(n+1)]
for a, b, c in edges:
    g[a].append((c, b))
    g[b].append((c, a))

#pprint(g)

# 프림 알고리즘
res = 0
used_e = 0
visited = [False] * (n + 1)
visited[1] = True
heap = []

for cost, node in g[1]:
    heapq.heappush(heap, (cost, node))

while used_e < n - 1:
    cost, node = heapq.heappop(heap)
    if visited[node]:
        continue
    visited[node] = True
    res += cost
    used_e += 1
    for adj_cost, adj in g[node]:
        if not visited[adj]:
            heapq.heappush(heap, (adj_cost, adj))

print(res)