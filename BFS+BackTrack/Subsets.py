'''
고유 요소 수의 정수 배열이 주어지면 가능한 모든 하위 집합(멱집합)을 반환합니다.
솔루션 세트에는 중복된 하위 세트가 포함되어서는 안 됩니다.
어떤 순서로든 솔루션을 반환합니다.
https://leetcode.com/problems/subsets/
'''
from collections import deque
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):
            res.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])

        dfs(0,[])
        return res




