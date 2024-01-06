import heapq

min_heap = []
result = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(min_heap) != 0:
            result.append(heapq.heappop(min_heap))
        else:
            result.append(0)
    else:
        heapq.heappush(min_heap, x)

print('\n'.join([str(re) for re in result]))