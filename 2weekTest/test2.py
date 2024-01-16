# Success
import collections
import sys
from collections import deque
from pprint import pprint

n = int(input())
picture = [list(sys.stdin.readline().replace('\n', '')) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if (0 <= nx < len(picture) and 0 <= ny < len(picture[0])
                    and picture[nx][ny] == picture[x][y] and visited[nx][ny] == 0):
                q.append((nx, ny))
                visited[nx][ny] = 1

res = 0
disRes = 0

visited = [[0] * n for _ in range(n)]
checker = collections.defaultdict(int)

while 1:
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if visited[i][j] == 0:
                bfs(i, j)
                checker[picture[i][j]] += 1
                res += 1
    break

for i in range(len(picture)):
    for j in range(len(picture[0])):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
checker = collections.defaultdict(int)

while 1:
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if visited[i][j] == 0:
                bfs(i, j)
                checker[picture[i][j]] += 1
                disRes += 1
    break

print(res, disRes)
