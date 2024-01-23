'''
정수 배열 nums가 주어지면 합계가 가장 큰 하위 배열을 찾아 해당 합계를 반환합니다.
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        start = 1
        while start < len(nums):
            target = nums[start]
            acc = dp[-1]
            if target > target + acc:
                dp.append(target)
                start += 1
            else:
                dp.append(target + acc)
                start += 1

        return max(dp)

print(Solution().maxSubArray([5,4,-1,7,8]))