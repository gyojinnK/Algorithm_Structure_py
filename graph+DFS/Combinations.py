from typing import List
'''
두 개의 정수 n과 k가 주어지면 [1, n] 범위에서 선택한 k 숫자의 가능한 모든 조합을 반환합니다. 
어떤 순서로든 답변을 반환할 수 있습니다.
'''
# 조합!
# DFS 트리 이용
# 다음 Depth에서의 시작값.
# 트리를 트래버스 할 때 다음 시작점을 가지고 간다.
# 시작점: bw, 현재 1로 마무리 했다면 다음은 2가 시작점 -> 현재 시작점+1
# 다음 시작점을 함께 가지고 가야 다시 탐색하는 것을 방지 가능
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        # 순열과 차이점
        # 1. 모든 요소를 고정하여 재귀함수 수행
        # 2. 재귀함수를 수행할 때마다 시작 요소를 하나씩 증가시켜 다음 시작 요소부터 수행
        def dfs(elements, start, k):
            # 종료조건
            # k개의 조합만을 만들어야함
            if k == 0:
                res.append(elements[:])
                return

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)
        return res

s = Solution()
print(s.combine(4, 2))
