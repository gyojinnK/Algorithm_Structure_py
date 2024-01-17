def insertionSort(lst):
    for cur in range(1, len(lst)):
        for delta in range(1, cur + 1):
            cmp = cur - delta
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst

print(insertionSort([4, 6, 2, 9, 1]))