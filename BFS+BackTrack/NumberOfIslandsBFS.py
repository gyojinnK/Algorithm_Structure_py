from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '1':
                    continue
                else:
                    cnt += 1
                    q = deque([(i, j)])

                    while q:
                        x, y = q.popleft()
                        # 동서남북
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != '1':
                                continue
                            else:
                                grid[nx][ny] = '0'
                                q.append((nx, ny))
        return cnt

s = Solution()
print(s.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]))