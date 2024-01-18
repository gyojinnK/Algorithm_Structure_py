import heapq

t = int(input())
res = [0] * t
for i in range(t):
    k = int(input())
    fSizes = list(map(int, input().split()))
    heapq.heapify(fSizes)
    for _ in range(k - 1):
        a = heapq.heappop(fSizes)
        b = heapq.heappop(fSizes)
        res[i] += a + b
        heapq.heappush(fSizes, a + b)

print('\n'.join(str(r) for r in res))