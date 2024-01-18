from heapq import *

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

heapify(lectures)
temp = []
for i in range(len(lectures)):
    start, end = heappop(lectures)
    temp.append((start, end))

