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

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input())

g = []
totalCost = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        charToNum = ord(matrix[i][j])
        if 65 <= charToNum <= 90: # 대문자
            g.append(((charToNum - 38), i, j))
            totalCost += charToNum - 38
        elif 96 <= charToNum <= 122:   # 소문자
            g.append(((charToNum - 96), i, j))
            totalCost += charToNum - 96
        else:
            g.append((0, i, j))

g.sort()
minCost = 0
parents = list(range(n))
for cost, node, adj in g:
    if cost == 0:
        continue
    if find(node) != find(adj):
        union(node, adj)
        totalCost -= cost

check = set()
for i in range(n):
    if find(i) not in check:
        check.add(find(i))

if len(check) == 1:
    print(totalCost)
else:
    print(-1)

# if find(0) == find(n-1):
#     print(totalCost)
# else:
#     print(-1)