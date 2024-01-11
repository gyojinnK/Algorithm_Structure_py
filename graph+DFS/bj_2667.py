import sys

n = int(input())

map = []*n

for i in range(n):
    line = input()
    temp = []
    for t in line:
        temp.append(t)
    map.append(temp)

row = len(map)
col = len(map[0])

def dfs(i, j):
    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]) or map[i][j] != '1':
        return
    else:
        map[i][j] = '#'

        # 4방향 탐색
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i-1, j)

cnt = 0
for i in range(row):
    for j in range(col):
        if map[i][j] == '1':
            dfs(i, j)
            cnt += 1

print(cnt)

# 단지 수는 구함
# 단지별 집 수를 못구함...
