from pprint import pprint

n = int(input())    # 회의의 수
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((e, s))

lst.sort()

res = 0
now = 0 # 마지막으로 확인한 시간
for end, start in lst:
    if now <= start:
        now = end
        res += 1

print(res)