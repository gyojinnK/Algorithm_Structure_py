import heapq

n = int(input())    # 컴퓨터의 수
m = int(input())    # 선의 수
edges = [tuple(map(int, input().split())) for _ in range(m)]
g = [[] for _ in range(n + 1)]

for a, b, c in edges:
    g[a].append((c, b))
    g[b].append((c, a))

visited = [False] * (n + 1)
# 임의의 정점을 시작으로 선택 (1)
visited[1] = True
heap = []
# 시작으로 선택한 정점의 간선(adj), 가중치(cost)를 탐색 대상에 추가한다. (heap에 추가)
for cost, adj in g[1]:
    heapq.heappush(heap, (cost, adj))

res = 0
used_e = 0
# 종료 조건:
# 트리를 구성해야 함으로 사이클이 없는 간선 개수 만큼 돈다.
while used_e < n - 1:
    cost, v = heapq.heappop(heap)
    if visited[v]:
        continue
    # 방문 처리, cost 계산, 간선 사용 처리
    visited[v] = True
    res += cost
    used_e += 1
    # 현재 정점과 연결된 정점들을 탐색 대상에 추가
    for cost, adj in g[v]:
        if not visited[adj]:
            heapq.heappush(heap, (cost, adj))

print(res)


