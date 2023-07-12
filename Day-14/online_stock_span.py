def __init__(self):
    self.stack = []

def next(self, price: int) -> int:
    result = 1
    while self.stack and self.stack[-1][0] <= price:
        result += self.stack.pop()[1]
    self.stack += [[price,result]]
    return result