def flatten(root):
    #Your code here
    def mergeTwoLinkedList(a,b):
        temp = Node(0)
        res = temp
        
        while a and b:
            if a.data < b.data:
                temp.bottom = a
                temp = temp.bottom
                a = a.bottom
            else:
                temp.bottom = b
                temp = temp.bottom
                b = b.bottom
        if a:
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
    
        return res.bottom
    
    if not root or not root.next:
        return root
    
    root = mergeTwoLinkedList(root,flatten(root.next))
    return root