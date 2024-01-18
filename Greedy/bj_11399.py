n = int(input())
p = list(map(int, input().split()))
p.sort()
nowWait = 0
res = []
for i in p:
    nowWait += i
    res.append(nowWait)

print(sum(el for el in res))
