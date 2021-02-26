def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        while j >= 0:
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
    return arr