'''
수강해야 하는 총 numCourses 강좌가 있으며 0부터 numCourses - 1까지 레이블이 지정됩니다.
prerequisites[i] = [ai, bi]는 수강하려는 경우 먼저 bi 강좌를
수강해야 함을 나타내는 배열 전제 조건이 제공됩니다. 물론이지.
예를 들어, [0, 1] 쌍은 코스 0을 수강하려면 먼저 코스 1을 수강해야 함을 나타냅니다.
모든 과정을 완료할 수 있으면 true를 반환합니다. 그렇지 않으면 false를 반환합니다.
'''
import collections
from typing import List

# 순환 구조인지 확인
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # 중복 방문이 발생한다. == 순환 구조이다.
        traced = set()
        visited = set()

        def dfs(v):
            if v in traced:
                return False
            # 이미 방문했던 노드면 True
            if v in visited:
                return True

            traced.add(v)
            for y in graph[v]:
                if not dfs(y):
                    return False
            # 특정 경우 순환 구조가 아니지만 순환 구조로 잘못 판단하는 경우 발생
            # 이전 방문 노드는 삭제
            traced.remove(v)
            # 탐색 종료 후 방문 노드 추가
            visited.add(v)
            return True

        # 순환 구조 판별 시작
        # list(graph)로 키값 가져오기
        for x in list(graph):
            if not dfs(x):
                return False

        return True

s = Solution()
print(s.canFinish(2, [[1,0]]))

