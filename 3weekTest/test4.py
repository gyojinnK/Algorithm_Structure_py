import collections
import heapq

n, m = map(int, input().split())
g = collections.defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

f1, f2 = map(int, input().split())

def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = collections.defaultdict(int)

    while q:
        acc, cur = heapq.heappop(q)
        if cur not in dist:
            dist[cur] = acc
            for adj, weight in g[cur]:
                accWeight = acc + weight
                heapq.heappush(q, (accWeight, adj))

    return dist

possible = dijk(f1)
print(possible[f2])

