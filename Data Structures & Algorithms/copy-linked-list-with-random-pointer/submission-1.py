class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_to_copy = {}

        # Pass 1: Create a copy of every node
        cur = head

        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next

        # Pass 2: Connect next and random pointers
        cur = head

        while cur:
            copy = old_to_copy[cur]

            copy.next = old_to_copy.get(cur.next)
            copy.random = old_to_copy.get(cur.random)

            cur = cur.next

        return old_to_copy.get(head)