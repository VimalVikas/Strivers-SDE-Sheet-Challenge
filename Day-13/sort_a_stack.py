def sort(stack,elem):
    if len(stack) == 0 or (len(stack) > 0 and stack[-1] < elem):
        stack.append(elem)
        return
    num = stack.pop()
    sort(stack,elem)
    stack.append(num)
    
def solve(stack):
    if len(stack) == 0:
        return
    elem = stack.pop()
    solve(stack)
    sort(stack,elem)
solve(stack)