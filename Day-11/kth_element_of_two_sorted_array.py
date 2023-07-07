def kthElement(self,  arr1, arr2, n, m, k):
    arr3 = arr1+arr2 
    arr3.sort()
    return arr3[k-1]