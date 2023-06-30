def getInversions(arr, n) :
    def merge(arr,temp,left,mid,right):
        inv_count = 0
        i = left
        j = mid 
        k = right
        temp = [0]
        while (i <= mid-1) and j <= right:
            if(arr[i] <= arr[j]):
                temp[k] = arr[i]
                k += 1
                i += 1
            else:
                temp[k] = arr[j]
                k += 1
                j += 1
                inv_count = inv_count +(mid-i)
        while i <= mid-1:
            temp[k] = arr[i]
            k += 1
            i += 1
        while j <= right:
            temp[k] = arr[j]
            k += 1
            j += 1
        for i in range(left,right):
            arr[i] = temp[i]
        return inv_count
    
    def merge_sort(arr,left,right):
        int_count = 0
        if left < right:
            mid = int((left+right)/2)
            inv_count = merge_sort(arr,left,mid)
            inv_count += merge_sort(arr,mid+1,right)
            inv_count += merge(arr,left,mid+1,right)
        return inv_count
	# Write your code here.
	return merge_sort(arr,0,n-1)