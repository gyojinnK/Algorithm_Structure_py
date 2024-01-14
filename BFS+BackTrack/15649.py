import itertools

n, m = map(int, input().split())

nums = []
for i in range(1, n+1):
    nums.append(i)

res = itertools.permutations(nums, m)

for els in res:
    print(' '.join(str(e) for e in els))