from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        p = []
        while head is not None:
            p.append(head.val)
            head = head.next

        while len(p) > 1:
            if p.pop(0) != p.pop():
                return False

        return True