# 정수 배열 nums와 정수 k가 주어지면 배열에서 k번째로 큰 요소를 반환합니다.
# 이는 정렬된 순서에서 k번째로 큰 요소이지 k번째 고유 요소가 아닙니다.
# "정렬"하지 않고 해결할 수 있나요?
# -> max heap 사용 문제
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        result = 0
        for num in nums:
            heapq.heappush(max_heap, -num)

        for _ in range(k):
            result = -heapq.heappop(max_heap)

        return result

s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))