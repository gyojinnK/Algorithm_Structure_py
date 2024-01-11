'''
고유한 정수의 배열이 주어지면 가능한 모든 순열을 반환합니다. 어떤 순서로든 답변을 반환할 수 있습니다.
'''
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] # 순열 조합이 완성되면 저장
        path = [] # 각 재귀 호출 마다 순열 저장

        def dfs(nums):
            if len(nums) == 0:
                res.append(path[:])

            for e in nums:
                next = nums[:]
                next.remove(e)

                path.append(e)
                dfs(next)
                path.pop()

        dfs(nums)
        return res

s = Solution()
print(s.permute([1,2,3]))