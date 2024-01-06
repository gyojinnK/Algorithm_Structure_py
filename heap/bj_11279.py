import heapq

max_heap = []
result = []

n = int(input())
for i in range(n):
    x = int(input())

    # x=0 : 큰 값 추출
    if x == 0:
        # 비어 있는 경우
        if not max_heap:
            result.append(0)
        else:
            # max heap -> -값으로 삽입 -> -(값)으로 추출
            result.append(-heapq.heappop(max_heap))
    # x!=0 : x값 삽입
    else:
        heapq.heappush(max_heap, -x)

print('\n'.join([str(res) for res in result]))