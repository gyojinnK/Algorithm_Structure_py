'''
빨간색, 흰색 또는 파란색으로 색상이 지정된 n개의 개체가 포함된 배열 nums가 주어지면
동일한 색상의 개체가 빨간색, 흰색, 파란색 순서로 인접하도록 해당 위치에서 정렬합니다.
우리는 정수 0, 1, 2를 사용하여 각각 빨간색, 흰색, 파란색을 나타냅니다.
라이브러리의 정렬 기능을 사용하지 않고 이 문제를 해결해야 합니다.
'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def merge(arr1, arr2):
            res = []
            i = j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1

            while i < len(arr1):
                res.append(arr1[i])
                i += 1

            while j < len(arr2):
                res.append(arr2[j])
                j += 1

            return res

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        l = nums[:mid]
        r = nums[mid:]
        return merge(self.sortColors(l), self.sortColors(r))


print(Solution().sortColors([2,0,2,1,1,0]))