class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current = head
        nodes = []
        while current:
            nodes.append(current)
            current = current.next
        nodes.pop(-1*n)
        if nodes:
            head = nodes[0]
            current = head
            for node in nodes:
                current.next = node
                current = current.next
            current.next = None
            return head
        return None

