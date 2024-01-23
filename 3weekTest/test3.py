import collections
import heapq

# n: 학생 수
# m: 단방향 도로(간선)
# x: 파티를 여는 마을(도착 지점)
n, m, x = map(int, input().split())
g = collections.defaultdict(list)

for _ in range(m):
    s, e, c = map(int, input().split())
    g[s].append((e, c))

def dijk(start):
    q = []
    dist = collections.defaultdict(int)
    heapq.heappush(q, (0, start))
    while q:
        acc, cur = heapq.heappop(q)
        if cur not in dist:
            dist[cur] = acc
            for adj, d in g[cur]:
                cost = acc + d
                heapq.heappush(q, (cost, adj))

    return dist

res = 0
for i in range(1, n + 1):
    ins = dijk(i)
    outs = dijk(x)
    res = max(res, ins[x] + outs[i])

print(res)