def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    iters = front = head

    while iters:
        front = iters.next
        copy = Node(iters.val)
        iters.next = copy
        copy.next = front
        iters = front
    iters = head
    while iters:
        if iters.random:
            iters.next.random = iters.random.next
        iters = iters.next.next
    dummy = Node(0)
    temp = dummy
    iters = front = head
    while iters:
        front = iters.next.next
        temp.next = iters.next
        iters.next = front
        temp = temp.next
        iters = front
    return dummy.next