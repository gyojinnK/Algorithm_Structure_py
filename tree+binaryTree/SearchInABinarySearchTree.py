'''
BST(이진 검색 트리)의 루트와 정수 값이 제공됩니다.
노드의 값이 val과 동일한 BST에서 노드를 찾고 해당 노드를 루트로 하는 하위 트리를 반환합니다.
해당 노드가 없으면 null을 반환합니다.
'''
import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val: int) -> Optional[TreeNode]:
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

        while root:
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    return
            elif root.val > val:
                if root.left:
                    root = root.left
                else:
                    return
            else:
                return root

print(Solution().searchBST([4,2,7,1,3], 2))
