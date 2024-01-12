from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def make_tree(lst, idx):
            parent = None
            if idx < len(lst):
                value = lst[idx]
                if value is None:
                    return
                parent = TreeNode(value)
                parent.left = make_tree(lst, 2 * idx + 1)
                parent.right = make_tree(lst, 2 * idx + 2)

            return parent
        def invert(parent):
            if parent:
                parent.left, parent.right = invert(parent.right), invert(parent.left)
                return parent
        def make_lst_by(root):
            if not root:
                return []

            lst = []
            q = deque([root])

            while q:
                node = q.popleft()
                lst.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return lst

        root = make_tree(root, 0)
        return make_lst_by(invert(root))


print(Solution().invertTree([4,2,7,1,3,6,9]))