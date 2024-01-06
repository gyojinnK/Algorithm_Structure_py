# 1(군인을 나타냄)과 0(민간인을 나타냄)으로 구성된 m x n 이진 행렬 매트가 제공됩니다.
# 군인들은 민간인 앞에 배치됩니다. 즉, 모든 1은 각 행의 모든 1은 각 행의 모든 0 왼쪽에 나타납니다.
# 다음 중 하나가 참인 경우 행 i는 행 j보다 약합니다.
# 1. i행의 군인 수는 j행의 군인 수보다 적습니다.
# 2. 두 행 모두 군인 수는 같고 i < j입니다.
# 가장 약한 것부터 강한 것 순으로 행렬에서 가장 약한 k개 행의 인덱스를 반환합니다.
import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        res = []

        for i, el in enumerate(mat):
            soldiers = el.count(1)
            # 군인의 수, 인덱스 순서로 리스트에 저장
            min_heap.append([soldiers, i])

        # 리스트를 힙으로 전환
        # 최소 힙
        heapq.heapify(min_heap)

        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res

s = Solution()
print(s.kWeakestRows([[1,1,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,0],
                    [1,1,0,0,0],
                    [1,1,1,1,1]], 3))