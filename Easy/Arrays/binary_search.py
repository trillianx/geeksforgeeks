def binary_search(arr, value):
    n = len(arr)
    if n < 1:
        return False 
    mid = n // 2
    if value == arr[mid]:
        return True
    elif value < arr[mid]:
        return binary_search(arr[:mid], value)
    else:
        return binary_search(arr[mid+1:], value)
    return False