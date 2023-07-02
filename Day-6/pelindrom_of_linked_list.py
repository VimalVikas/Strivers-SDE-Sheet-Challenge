def isPalindrome(self, head: Optional[ListNode]) -> bool:
    slow = fast = entry = head

    def reverseLinkedList(node):
        cur = front = node
        prev = None

        while cur:
            front = cur.next
            cur.next = prev
            prev = cur
            cur = front
    
        return prev

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    slow = reverseLinkedList(slow.next)

    while slow:
        if slow.val != entry.val:
            return False
        entry = entry.next
        slow = slow.next

    return True