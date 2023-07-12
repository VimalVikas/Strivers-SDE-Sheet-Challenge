def __init__(self):
    self.stack = deque()
    self.minStack = deque()

def push(self, val: int) -> None:
    self.stack.append(val)
    if self.minStack:
        self.minStack.append(
            min(val, self.minStack[-1])
            )
    else:
        self.minStack.append(val)

def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

def top(self) -> int:
    return self.stack[-1]

def getMin(self) -> int:
    return self.minStack[-1]
    
