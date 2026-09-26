# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        nodes = []
        current = head
        while current:
            nodes.append(current.val)
            current = current.next
        nodes.sort()
        head = ListNode(nodes[0])
        current = head
        for item in nodes[1:]:
            current.next = ListNode(item)
            current = current.next
        return head