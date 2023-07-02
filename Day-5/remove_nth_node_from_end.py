def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    slow = dummy
    fast = dummy 
    
    for i in range(n):
        fast = fast.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    slow.next= slow.next.next

    return dummy.next
