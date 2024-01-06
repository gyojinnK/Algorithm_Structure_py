'''
[물이 가장 많은 용기]
길이 n의 정수 배열 높이가 제공됩니다.
i번째 선의 두 끝점이 (i, 0)과 (i, height[i])가 되도록 n개의 수직선이 그려집니다.
x축과 함께 용기를 형성하는 두 개의 선을 찾아 용기에 가장 많은 물이 포함되도록 하세요.
컨테이너가 저장할 수 있는 최대 물의 양을 반환합니다.
용기를 기울일 수는 없습니다.
'''
from typing import List

# 투포인터로 해결
# 배열 관련 문제에서 시간초과가 나온다면
# 대부분 슬라이딩 윈도우나 투포인터로 해결 가능
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_amount = 0

        while left < right:
            cur_amount = min(height[left], height[right]) * (right - left)
            max_amount = max(max_amount, cur_amount)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_amount



# # 시간 초과
# class Solution:
#     # (두 선분사이의 거리) * (두 선분 중 더 작거나 같은 선분의 높이)
#     # 위의 식의 값이 최대가 되는 값
#     def max_area(self, height: List[int]) -> int:
#         #
#         def calcAmount(h1, i1, h2, i2) -> int:
#             width = i2 - i1
#             height = h1 if h1 < h2 else h2
#             return width * height
#
#         max_amount = 0
#         for i in range(len(height)-1):
#             for j in range(1, len(height)):
#                 max_amount = max(max_amount, calcAmount(height[i], i, height[j], j))
#
#         return max_amount

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))