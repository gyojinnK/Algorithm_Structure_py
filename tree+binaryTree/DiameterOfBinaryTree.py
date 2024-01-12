'''
이진 트리의 루트가 주어지면 트리 지름의 길이를 반환합니다.
이진 트리의 직경은 트리의 두 노드 사이에서 가장 긴 경로의 길이입니다.
이 경로는 루트를 통과할 수도 있고 통과하지 않을 수도 있습니다.
두 노드 사이의 경로 길이는 두 노드 사이의 간선 수로 표시됩니다.
'''
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def make_bt(lst, idx):
            parent = None
            if idx < len(lst):
                value = lst[idx]
                if not value:
                    return

                parent = TreeNode()
                parent.left = make_bt(lst, 2 * idx + 1)
                parent.right = make_bt(lst, 2 * idx + 2)

            return parent

        root_bt = make_bt(root, 0)

        if not root_bt:
            return 0
        q = deque([root_bt])

        maxDepth = 0
        while q:
            maxDepth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return maxDepth


print(Solution().diameterOfBinaryTree([1,2]))
