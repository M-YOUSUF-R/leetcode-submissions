# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        digit1= ""
        digit2= ""
        current = l1
        while  current:
            digit1 += str(current.val)
            current = current.next
        current = l2
        while current:
            digit2 += str(current.val)
            current = current.next
        
        digit1 = int(digit1[::-1])
        digit2 = int(digit2[::-1])
        out = digit1 + digit2
        out = str(out)
        out = out[::-1]
        head = ListNode(int(out[0]))
        current = head
        for ch in out[1:]:
            current.next = ListNode(int(ch)) 
            current = current.next
        return head
