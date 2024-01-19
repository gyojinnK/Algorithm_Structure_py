n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
res = 0
while 1:
    mid = (start + end) // 2
    cnt = 0
    if start > end:
        res = mid
        break

    for t in trees:
        if t > mid:
            cnt += t - mid

    if cnt == m:
        res = mid
        break
    elif cnt > m:
        start = mid + 1
    else:
        end = mid - 1

print(res)