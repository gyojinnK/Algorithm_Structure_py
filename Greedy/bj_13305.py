# 부분 성공
n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

# print(distances)
# print(costs)
res = 0
now = 0

while True:
    if now >= len(costs) - 1:
        break
    if now == len(costs) - 2:
        res += costs[now] * distances[now]
        break
    near = costs[now] * distances[now]
    jump = costs[now] * (distances[now] + distances[now+1])
    batch = costs[now] * distances[now] + costs[now+1] * distances[now+1]
    if jump > batch:
        res += near
        now += 1
        # i += 1
    else:
        res += jump
        now += 2
        # i += 2

print(res)