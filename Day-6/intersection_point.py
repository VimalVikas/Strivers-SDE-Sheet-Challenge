def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    l1 = headA
    l2 = headB

    while l1 != l2:
        l1 = headB if l1 is None else l1.next
        l2 = headA if l2 is None else l2.next
    return l1