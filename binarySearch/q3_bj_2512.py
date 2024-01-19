import bisect

n = int(input())
budgets = list(map(int, input().split()))
totalBudget = int(input())

start = 0
end = max(budgets)

while start <= end:
    # 중간값(예산)
    mid = (start + end) // 2
    budgetCnt = 0
    for b in budgets:
        # 예산이 중간 예산보다 많으면 중간 예산 배정
        if b > mid:
            budgetCnt += mid
        # 적다면 그대로 배정
        else:
            budgetCnt += b

    if budgetCnt <= totalBudget:
        # 배정 예산이 총 예산보다 적으면 중간 예산 늘리기 (더 많이 줄 수 있음)
        start = mid + 1
    else:
        # 초과 시 예산 줄이기
        end = mid - 1


print(end)