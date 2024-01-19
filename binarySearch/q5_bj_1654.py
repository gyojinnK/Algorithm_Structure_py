# k: 이미 갖고 있는 랜선 수
# n: 필요한 랜선 수
k, n = map(int, input().split())
kList = list(int(input()) for _ in range(k))
res = 0
start = 1
end = max(kList)

while 1:
    # 자를 길이 설정
    mid = (start + end) // 2
    possibleCnt = 0

    if start > end:
        res = mid
        break

    for l in kList:
        if l // mid != 0:
            cut = l // mid
            possibleCnt += cut

    if possibleCnt < n:
        end = mid - 1
    elif possibleCnt >= n:
        start = mid + 1
    else:
        res = mid
        break

print(res)