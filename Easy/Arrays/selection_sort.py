def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_val = arr[i]
        min_index = i
        for j in range(i+1,n):
            if arr[j] < min_val:
                min_index = j
                min_val = arr[j]
        print(arr[min_index], min_index)
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr