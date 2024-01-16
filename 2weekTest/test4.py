# 문제 4. 스티커 붙이기
from pprint import pprint

n, m, k = map(int, input().split())
noteBook = [[0] * m for _ in range(n)]

for _ in range(k):
    ri, ci = map(int, input().split())
    sticker = []
    for i in range(ri):
        sticker.append(list(map(int, input().split())))


