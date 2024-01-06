import collections
import sys

n, m = map(int, sys.stdin.readline().split())
db = collections.defaultdict(str)
res = []

for _ in range(n):
    addr, pw = map(str, input().split())
    db[addr] = pw

for _ in range(m):
    target = input()
    res.append(db[target])

print('\n'.join([pw for pw in res]))