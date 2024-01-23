n, m = map(int, input().split())
books = list(map(int, input().split()))

plus = []
minus = []
cnt = []

for i in books:
    if i > 0:
        plus.append(i)
    else:
        minus.append(abs(i))

plus.sort(reverse=True)
minus.sort(reverse=True)

for i in range(len(plus)//m):
    cnt.append(plus[i * m])

if len(plus) % m > 0:
    cnt.append(plus[(len(plus) // m) * m])

for i in range(len(minus) // m):
    cnt.append(minus[i * m])

if len(minus) % m > 0:
    cnt.append(minus[(len(minus) // m) * m])

cnt.sort()

res = cnt.pop()
res += 2 * sum(cnt)

print(res)