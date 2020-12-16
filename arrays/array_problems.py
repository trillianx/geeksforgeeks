# These are Must Do Coding Questions

"""
Question 1. Given an unsorted array A of size N of non-negative integers,
find a continuous sub-array which adds to a given number S
"""
def find_subarray(S, arr):
    result = []
    start = 0
    sum_val = 0
    for end in range(len(arr)):
        sum_val += arr[end]
        while sum_val >= S:
            if sum_val == S:
                result.append(arr[start:end+1])
            sum_val = sum_val - arr[start]
            start += 1
    if len(result) == 0:
        return -1
    return result

if __name__ == "__main__":
    arr = [1, 5, 2, 3, 2, 8, 3, 1, 4]
    S = 8
    result = find_subarray(S, arr)
    print(result)