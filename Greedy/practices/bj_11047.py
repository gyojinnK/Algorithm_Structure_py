n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    if coin > k:
        continue
    else:
        coins.append(coin)

res = 0
check = 0
while k != 0:
    if coins[-1] <= k:
        k -= coins[-1]
        res += 1
    else:
        coins.pop()

print(res)