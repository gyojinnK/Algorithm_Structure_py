from typing import List

'''
'1'(땅)과 '0'(물)의 지도를 나타내는 m x n 2D 이진 그리드 그리드가 주어지면 섬의 수를 반환합니다.
섬은 물로 둘러싸여 있으며 인접한 육지가 수평 또는 수직으로 연결되어 형성됩니다.
그리드의 네 모서리가 모두 물로 둘러싸여 있다고 가정할 수 있습니다.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if (i < 0 or i >= len(grid) or j < 0 or
                    j >= len(grid[0]) or grid[i][j] != '1'):
                return

            grid[i][j] = 0

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    cnt += 1
        return cnt

s = Solution()
res = s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])

print(res)

