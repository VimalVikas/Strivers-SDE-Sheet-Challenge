def __init__(self, root):
    self.cur = root
def hasNext(self):
    return True if self.cur else False   
def next(self):
    while self.cur:
        if self.cur.left == None:
            res = self.cur.val
            self.cur = self.cur.right
            return res
        else:
            prev = self.cur.left
            while prev.right != None and prev.right != self.cur:
                prev = prev.right
        
            if prev.right == self.cur:
                prev.right = None
                res = self.cur.val
                self.cur = self.cur.right
                return res
        
            else:
                prev.right = self.cur
                self.cur = self.cur.left