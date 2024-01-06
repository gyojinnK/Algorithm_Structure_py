import collections
import sys

n = int(input())
ns = list(map(int, sys.stdin.readline().split()))
m = int(input())
ms = list(map(int, sys.stdin.readline().split()))

for num in ms:
    print(1 if num in ns else 0)

dict = collections.defaultdict(int)
print(dict)
