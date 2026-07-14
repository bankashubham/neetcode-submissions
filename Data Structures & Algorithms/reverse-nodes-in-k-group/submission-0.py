# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next
            groupStart = groupPrev.next

            curr = groupStart
            prev = groupNext

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            groupPrev.next = prev
            groupPrev = groupStart

        return dummy.next

    def getKth(self, node, k):
        for _ in range(k):
            if not node.next:
                return None
            node = node.next
        return node

