'''
m x n 정수 행렬 행렬에서 목표 값을 검색하는 효율적인 알고리즘을 작성하세요.
이 행렬에는 다음과 같은 속성이 있습니다.
각 행의 정수는 왼쪽에서 오른쪽으로 오름차순으로 정렬됩니다.
각 열의 정수는 위에서 아래로 오름차순으로 정렬됩니다.
'''
import bisect
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        for i in range(len(matrix)):
            row = matrix[i]
            tIdx = bisect.bisect_left(row, target)
            if tIdx < len(row) and row[tIdx] == target:
                res = True
                break
        return res

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))