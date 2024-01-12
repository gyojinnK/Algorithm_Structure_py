n = int(input())    # 노드의 개수
nodes = list(map(int, input().split()))
target = int(input())
cnt = 0

def dfs(target, nodes):
    # '#'은 삭제를 의미
    nodes[target] = '#'
    for i in range(len(nodes)):
        # 해당 인덱스의 노드 배열의 값이 지워진 부모 노드와 같다면
        if target == nodes[i]:
            dfs(i, nodes)

dfs(target, nodes)
print(nodes)
for i in range(len(nodes)):
    # nodes는 부모 노드를 입력 받은 배열
    # -> nodes 안에 없으면 부모노드가 아닌 리프노드라고 판단
    if nodes[i] != '#' and i not in nodes:
        cnt += 1

print(cnt)