from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            next, head.next = head, None
            prev, head = head, next

        return prev


s = Solution()
s.reverseList()
