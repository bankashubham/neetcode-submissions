# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None

        curr = list2
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        first, second = head, prev

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        