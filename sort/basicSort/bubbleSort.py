def bubbleSort(lst):
    # 최댓값을 구하는 알고리즘을 len(lst) - 1 만틈 반복
    iters = len(lst) - 1
    for iter in range(iters):
        # 이미 구한 최댓값은 범위에서 제외한다.
        wall = iters - iter
        # wall = len(lst)-1 - 1
        # wall = len(lst)-6
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]
    return lst

print(bubbleSort([4, 6, 2, 9, 1]))