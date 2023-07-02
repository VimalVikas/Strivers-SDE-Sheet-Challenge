def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    prev = None
    front = head

    while cur:
        front = cur.next
        cur.next = prev
        prev = cur
        cur = front
    return prev