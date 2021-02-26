def find_pivot(arr, low, high):
    # Base Case
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high / 2))

    # Check if mid is the pivot:
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    # Check if value before mid is the pivot
    if mid > low and arr[mid] < arr[mid-1]:
        return mid-1
    # Check if left subset 
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    else:
        return find_pivot(arr, mid+1, high)


    

if __name__=='__main__':
    arr = [73, 85, 94, 21, 27, 34, 47, 54, 66]
    print(find_pivot(arr, 0, len(arr)-1))