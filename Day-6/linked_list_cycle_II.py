def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = entry = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            while slow != entry:
                slow = slow.next 
                entry = entry.next
            return slow
    return None