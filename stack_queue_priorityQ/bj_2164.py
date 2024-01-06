from collections import deque
def solution(N):
    deq = deque([i for i in range(1, N+1)])
    while len(deq) > 1:
        deq.popleft()
        restore = deq.popleft()
        deq.append(restore)

    print(deq.popleft())

solution(6)