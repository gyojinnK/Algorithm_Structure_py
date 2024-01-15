from collections import deque
field = list()

for _ in range(12):
    row = list(input())
    field.append(row)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 탐색 함수
def bfs(i, j):
    q = deque()
    q.append((i, j))
    isDestroyCnt.append((i, j))
    while q:
        x, y = q.popleft()
        # 4방향 탐색
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            # 범위 내의 인덱스이며 색이 같고 아직 방문 안했다면 통과
            if (0 <= nx < 12 and 0 <= ny < 6 and
                    field[nx][ny] == field[x][y] and visited[nx][ny] == 0):
                # 탐색 대상 추가
                q.append((nx, ny))
                # 4개 이상인지 판별하기 위해서 추가
                isDestroyCnt.append((nx, ny))
                # 방문 처리
                visited[nx][ny] = 1

# 떨어지는 함수
def fall():
    # field 하단을 기준으로 체크
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if field[j][i] != '.' and field[k][i] == '.':
                    field[k][i] = field[j][i]
                    field[j][i] = '.'
                    break

# 파괴하는 함수
def destroy(isDestroyCnt):
    for i, j in isDestroyCnt:
        field[i][j] = '.'

res = 0
while 1:
    check = False
    visited = [[0]*len(field[0]) for _ in range(len(field))]
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] != '.' and visited[i][j] == 0:
                # 방문 처리
                visited[i][j] = 1
                # 조건을 만족하는 해당 색깔의 뿌요가 몇개 인접하는지 카운트하는 리스트
                isDestroyCnt = []
                bfs(i, j)
                if len(isDestroyCnt) >= 4:
                    check = True
                    destroy(isDestroyCnt)
    if not check:
        break
    fall()
    res += 1

print(res)

