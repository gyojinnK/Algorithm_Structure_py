import heapq
import sys

# 테스트 케이스 수
T = int(input())
res = []
while T > 0:
    heap = []
    n, m = map(int, sys.stdin.readline().split())
    b = list(map(int, input().split()))
    for i in range(len(b)):
        # [가중치, 인덱스]
        # '-'로 최대 힙 사용
        item = [-b[i], i]
        heapq.heappush(heap, item)

    cnt = 0
    for i in range(len(heap)):
        cnt += 1
        if heapq.heappop(heap)[1] == m:
            break
    res.append(cnt)
    cnt = 0

    T -= 1

print('\n'.join([str(el) for el in res]))

# 오답
# 1. 힙 이용
# 2. 동일 가중치 처리 못함
# -> 큐 이용하기