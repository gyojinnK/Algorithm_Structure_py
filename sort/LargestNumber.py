'''
음수가 아닌 정수 숫자 목록이 주어지면 가장 큰 숫자를 형성하도록 배열하여 반환합니다.
결과가 매우 클 수 있으므로 정수 대신 문자열을 반환해야 합니다.
'''
import functools
import itertools
from pprint import pprint
from typing import List


class Solution:
    def ctk(self, a, b):
        # a = 3, b = 30
        #   330     303
        if a + b < b + a:
            return 1
        else:
            return -1
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(el) for el in nums]
        res = ''

        nums.sort(key=functools.cmp_to_key(self.ctk))
        # print(nums)

        if nums[0] == '0':
            return '0'

        for el in nums:
            res += el

        return res

print(Solution().largestNumber([3,30,34,5,9]))
