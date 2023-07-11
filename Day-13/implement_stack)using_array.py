def __init__(self, capacity: int):
    self._stack = [0]*capacity
    self._top = 0
    self._size = capacity

def push(self, num: int) -> None:
    if self._top >= self._size:
        return -1
    else:
        self._stack[self._top] = num
        self._top +=1
        return 1

def pop(self) -> int:
    if self._top == 0:
        return -1
    else:
        self._top-=1
        return self._stack[self._top]

def top(self) -> int:
    if self._top == 0:
        return -1
    else:
        return self._stack[self._top-1]

def isEmpty(self) -> int:
    if self._top == 0:
        return 1
    else:
        return 0

def isFull(self) -> int:
    if self._top == self._size+1:
        return 1
    else:
        return 0
    pass