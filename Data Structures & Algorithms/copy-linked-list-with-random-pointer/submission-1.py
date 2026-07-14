class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Insert copied nodes after each original node
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the two lists
        curr = head
        copyHead = head.next

        while curr:
            copy = curr.next

            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copyHead