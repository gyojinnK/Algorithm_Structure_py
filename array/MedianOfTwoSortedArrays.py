'''
Median of Two Sorted Arrays
각각 m과 n 크기의 두 개의 정렬된 배열 nums1과 nums2가 주어지면 두 개의 정렬된 배열의 중앙값을 반환합니다.
전체 런타임 복잡도는 O(log(m+n))여야 합니다.
'''
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        length = len(merged)
        middle = 0
        if length % 2 == 0:
            middle = (merged[length // 2 - 1] + merged[length // 2]) / 2.0
        else:
            middle = merged[length // 2]

        print(f'{middle:.5f}')

s = Solution()
s.findMedianSortedArrays([1,3], [2])