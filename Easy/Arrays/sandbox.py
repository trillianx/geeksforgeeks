def find_dups(arr):
    n = len(arr)
    start = 0
    for end in range(1, n):
        if arr[start] != arr[end]:
            start += 1
            arr[start] = arr[end]
    return arr[:start+1]
    

if __name__=='__main__':
    arr = [1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 7]
    print(find_dups(arr))