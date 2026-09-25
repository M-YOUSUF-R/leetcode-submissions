# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current = head
        ln = 0
        while current:
            ln += 1
            current = current.next
        if ln == 1 and n == 1:
            return None
        target = ln - n
        if target == 0:
            return head.next
        current = head
        for i in range(target - 1):
            current = current.next
        
        current.next = current.next.next
        return head if head else None
        
