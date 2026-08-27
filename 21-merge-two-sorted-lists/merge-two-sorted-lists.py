# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1        
        h2 = list2
        arr = []
        

        while h1:
            arr.append(h1.val)
            h1 = h1.next
        
        while h2:
            arr.append(h2.val)
            h2 = h2.next
        
        arr = sorted(arr)
        if not arr :
            return None
        
        head = ListNode(arr[0])
        curr = head
        for i in arr[1:]:
            n = ListNode(val=i)
            curr.next = n
            curr = curr.next
        
        return head

                
