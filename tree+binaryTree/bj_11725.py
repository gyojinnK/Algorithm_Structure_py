import collections

n = int(input())
tree = [[] for _ in range(n+1)]
res = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split(' '))
    tree[a].append(b)
    tree[b].append(a)

q = collections.deque([1])
while q:
    node = q.popleft()
    for i in tree[node]:
        if res[i] == 0:
            res[i] = node
            q.append(i)

print('\n'.join(str(res[i]) for i in range(2, len(res))))