# 가중치가 가장 큰 간선을 찾아 탐색하다가
# 시작 지점(숭이의 출발 위치)에서 도착 지점(혜빈의 위치)로 길이 완성되는 순간의
# 마지막 간선의 가중치를 구하자
# 가중치가 큰 간선 순서대로 유동적으로 탐색
# 그렇기 때문에 길에 연결(완성)된 시점의 마지막 가중치가 조건에 부합하는 최소 가중치가 된다.
# 유동적으로 그래프를 탐색하기 때문에 분리 집합과 신속한 비교와 유사 즉, 크루스칼 알고리즘을 이용!
from sys import stdin, setrecursionlimit

def find(parent, x):
    # parent[x] == x 즉, 자기 자신이 부모 정점
    if parent[x] == x:
        return x
    # **현재 parent[x]의 부모 정점을 찾아서 갱신(재귀)**
    parent[x] = find(parent, parent[x])
    return parent[x]

# 서로 다른 부모 정점을 갖는 집합 합치기
def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    # 이미 갖은 부모 노드라면 리턴
    if root_x == root_y:
        return
    # 아니라면 합치기
    parent[root_x] = root_y

input = stdin.readline
setrecursionlimit(10 ** 5)

n, m = map(int, input().split())
s, e = map(int, input().split())
edges = []
parent = list(range(n+1))
for _ in range(m):
    # 크루스칼 알고리즘은 가중치와 인접 노드를 하나에 담는다.
    x, y, k = map(int, input().split())
    # 가중치를 맨 앞에 삽입하는 이유: 가중치로 정렬
    edges.append((k, x, y))

# 모든 간선의 가중치를 기준으로 오름차순 정렬
edges.sort()
# n개의 정점에 대해 수행
# 최종적으로 찾는 마지막 간선의 가중치
last = 0

# 시작 지점의 부모 정점과 도착 지점의 부모 정점이 같지 않은 동안
while find(parent, s) != find(parent, e) and edges:
    # 가장 가중치가 높은 간선 먼저 확인
    # 오름차순 정렬 되어있기 때문에 뒤에서 pop
    d, x, y = edges.pop()
    last = d
    # union으로 같은 부모 정점으로 맞춰 나간다.
    union(parent, x, y)

print(last if find(parent, s) == find(parent, e) else 0)

