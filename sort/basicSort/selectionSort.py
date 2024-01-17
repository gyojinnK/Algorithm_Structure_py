def selectionSort(lst):
    # 반복 횟수 설정
    iters = len(lst) - 1
    for iter in range(iters):
        minimun = iter
        for cur in range(iter + 1, len(lst)):
            if lst[cur] < lst[minimun]:
                minimun = cur
        if minimun != iter:
            lst[minimun], lst[iter] = lst[iter], lst[minimun]

    return lst

selectionSort([4, 6, 2, 9, 1])