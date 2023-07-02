def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    run = dummy

    while list1 and list2:
        if list1.val < list2.val:
            run.next = list1
            list1, run = list1.next, list1
        else:
            run.next = list2
            list2,run = list2.next, list2
    if list1 or list2:
        run.next = list1 if list1 else list2
    
    return dummy.next