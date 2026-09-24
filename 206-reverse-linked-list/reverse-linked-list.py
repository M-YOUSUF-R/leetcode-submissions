# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        node = []
        current = head
        while current:
            node.append(current.val)
            current = current.next
        node.reverse()
        if not node:
            return None
        head = ListNode(node[0])
        current = head
        for i in node[1:]:
            current.next = ListNode(i)
            current = current.next
        return head