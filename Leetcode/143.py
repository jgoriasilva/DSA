from typing import *
from venv import create

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        prev = self.prev.val if self.prev else None
        val = self.val if self.val else None
        next = self.next.val if self.next else None
        return f'({prev}, {val}, {next})'

def createList(nums: List[int]) -> ListNode:
    dummy = ListNode()
    tail = dummy

    for num in nums:
        tail.next = ListNode(val=num)
        tail = tail.next

    return dummy.next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        prev = None 
        node = head
        while node:
            node.prev = prev
            # 3
            prev = node
            # 4
            node = node.next
            # None
        
        left = head
        # 2
        right = prev
        # 4

        tail = head
        # 1
        move_left = True
        # False
        while left != right:
            if move_left:
                tail.next = left
                left = left.next
                move_left = False
            else:
                tail.next = right
                # 4
                right = right.prev
                move_left = True
            tail = tail.next
            # 1
        tail.next = None
        tail = left.next

nums = [1, 2, 3, 4, 5]

head = createList(nums)
Solution().reorderList(head)