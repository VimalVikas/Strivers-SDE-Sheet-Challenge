def fractionalknapsack(self, W,arr,n):
    
    # code here
    arr.sort(key = lambda x: x.value/x.weight, reverse = True)
    
    value = 0
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            value += item.value
        else:
            remaining = W
            value += (item.value/item.weight)*remaining
            break
    return value