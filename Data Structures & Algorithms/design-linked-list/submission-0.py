class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)    # Left dummy node
        self.right = ListNode(0)   # Right dummy node

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next

        while curr != self.right and index > 0:
            curr = curr.next
            index -= 1

        if curr != self.right and index == 0:
            return curr.val

        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)

        next = self.left.next
        prev = self.left

        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)

        prev = self.right.prev      # Fixed
        next = self.right

        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next

        while curr and index > 0:   # Fixed (curr instead of cur)
            curr = curr.next
            index -= 1

        if curr and index == 0:
            node = ListNode(val)

            prev = curr.prev
            next = curr

            prev.next = node
            next.prev = node
            node.prev = prev
            node.next = next

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next

        while curr and index > 0:   # Fixed (curr instead of cur)
            curr = curr.next
            index -= 1

        if curr != self.right and index == 0:
            prev = curr.prev
            next = curr.next

            prev.next = next
            next.prev = prev