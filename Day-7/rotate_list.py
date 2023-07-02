def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return head
    cur = head
    length = 1

    while cur and cur.next:
        cur= cur.next
        length += 1
    
    cur.next = head
    k = k % length 
    k = length - k

    while k:
        cur = cur.next
        k -= 1
    head = cur.next
    cur.next = None
    return head