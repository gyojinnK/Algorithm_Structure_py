import collections

n = int(input())    # 홀수
nums = []
res = []
minSecond = 0
for _ in range(n):
    nums.append(int(input()))

nums.sort()

if len(nums) == 1:
    print(nums[0])
    print(nums[0])
    print(nums[0])
    print(0)

else:
    counter = collections.Counter(nums)
    mc = counter.most_common()
    _, maxCnt = mc[0]
    mc_list = []
    for el in mc:
        e, cnt = el
        if maxCnt <= cnt:
            mc_list.append((e, cnt))

    mc.sort()
    if len(mc_list) == 1:
        minSecond, _ = mc_list[0]
    else:
        minSecond, _ = mc_list[1]

    print(round(sum(nums) / n))
    print(nums[n // 2])
    print(minSecond)
    print(nums[-1] - nums[0])
