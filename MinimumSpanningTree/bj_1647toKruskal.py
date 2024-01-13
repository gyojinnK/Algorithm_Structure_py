n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
g = []
for a, b, c in edges:
    g.append((c, a, b))

parents = list(range(n+1))
g.sort()

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    parents[root_x] = root_y

res = 0
last = 0
# 반복문을 이용하여 가중치와 요소를 하나씩 꺼내서 find, union 수행
for c, x, y in g:
    # 조건문이 False라면 길로 이어졌다는 의미
    # 조건문이 True라면 이어지지 않았다는 의미로 union
    if find(x) != find(y):
        # 두 집합의 부모 정점을 연결해서 합치기
        union(x, y)
        res += c
        last = c

# 마지막 연결으 끊어 마을을 분리
print(res - last)
