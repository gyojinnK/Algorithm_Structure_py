'''
이진 트리의 루트가 주어지면 최대 깊이를 반환합니다.
이진 트리의 최대 깊이는 루트 노드에서 가장 먼 리프 노드까지 가장 긴 경로를 따라 있는 노드 수입니다.
'''
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, lst: Optional[TreeNode]) -> int:
        def make_tree_by(lst, idx):
            parent = None
            if idx < len(lst):
                value = lst[idx]
                if value is None:
                    return

                parent = TreeNode(value)
                parent.left = make_tree_by(lst, 2 * idx + 1)
                parent.right = make_tree_by(lst, 2 * idx + 2)

            return parent

        root = make_tree_by(lst, 0)
        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return depth

s = Solution()
print(s.maxDepth([3, 9, 20, None, None, 15, 7]))
