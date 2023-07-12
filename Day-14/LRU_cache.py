def __init__(self, capacity: int):
    self.capacity = capacity
    self.val = OrderedDict()

def get(self, key: int) -> int:
    if key not in self.val:
        return -1
    else:
        self.val[key] = self.val.pop(key)
        return self.val[key]

def put(self, key: int, value: int) -> None:
    if key not in self.val:
        if len(self.val) == self.capacity:
            self.val.popitem(last=False)
    else:
        self.val.pop(key)
    self.val[key] = value