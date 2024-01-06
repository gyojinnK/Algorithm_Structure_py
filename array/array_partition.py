def arrayPairSum(nums):
    nums.sort()
    group = []
    res = 0
    for i in range(len(nums)):
        group.append(nums[i])
        if len(group) == 2:
            res += min(group[0], group[1])
            group = []

    print(res)

arrayPairSum([6,2,6,5,1,2])