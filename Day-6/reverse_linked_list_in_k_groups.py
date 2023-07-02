def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def find_length(node):
        length = 0
        while node != None:
            node = node.next
            length += 1
        return length
            
    
    if head == None or head.next == None:
        return head
    
    length = find_length(head)

    dummy = ListNode()
    dummy.next = head

    prev = dummy
    cur = front = None

    while length >= k:
        cur = prev.next
        front = cur.next
        for i in range(1,k):
            cur.next = front.next
            front.next = prev.next
            prev.next = front
            front = cur.next
        length -= k
        prev = cur
    return dummy.next