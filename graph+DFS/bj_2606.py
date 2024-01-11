import sys

n = int(input())
conVal = int(input())

# 1~7번 컴퓨터
# 인덱스 0은 버림
graph = [[] for i in range(n+1)]

# 방문했다면 1 아니라면 0
# 마찬가지로 인덱스 0은 버림
visited = [0] * (n+1)

# 그래프 생성
for i in range(conVal):
    line = list(sys.stdin.readline().split())
    # graph[int(line[0])].append(int(line[1]))
    # 양방향
    graph[int(line[0])].append(int(line[1]))
    graph[int(line[1])].append(int(line[0]))

# print(graph)

# cv: 현재 방문 노드
def dfs(cv):
    visited[cv] = 1
    for el in graph[cv]:
        # 방문하지 않았다면
        if visited[el] == 0:
            # 탐색 ㄱㄱ
            dfs(el)

dfs(1)

# 모든 탐색이 끝나면
# 각 컴퓨터 방문 여부 (1 or 0) 모두 더하기
# 자신은 제외
print(sum(visited)-1)