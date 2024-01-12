'''
이진 검색 트리의 루트 노드와 두 개의 정수 low 및 high가 주어지면
값이 포함 범위 [low, high]에 있는 모든 노드 값의 합을 반환합니다.
'''
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def make_bst(lst, idx):
            parent = None
            if idx < len(lst):
                value = lst[idx]
                if value is None:
                    return
                parent = TreeNode(value)
                parent.left = make_bst(lst, 2 * idx + 1)
                parent.right = make_bst(lst, 2 * idx + 2)

            return parent

        root = make_bst(root, 0)

        q = collections.deque([root])
        vals = []
        res = 0

        while q:
            node = q.popleft()
            vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        sorted_vals = sorted(vals)
        start = sorted_vals.index(low)
        end = sorted_vals.index(high)

        for i in range(start, end+1):
            res += sorted_vals[i]

        return res


Solution().rangeSumBST([10,5,15,3,7,None,18], 7, 15)