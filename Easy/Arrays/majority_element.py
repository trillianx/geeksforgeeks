"""
Given an array A of N elements. Find the majority element in the array.
A majority element in an array A of size N is an element that appears
more than N/2 times in the array.

The task is to complete the function majorityElement()
which returns the majority element in the array. If no majority exists,
return -1.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.
"""
import math
def majorityElement(A, N):
    arr = A
    arr.sort()
    start = 0
    for end in range(1, N):
        if arr[start] != arr[end]:
            start += 1
    window_size = end - start + 1
    if window_size > N/2:
        return arr[start]
    else:
        return -1


def majority_element(arr):
    counter, possible_element = 0, None
    for i in arr:
        if counter == 0:
            possible_element, counter = i, 1
        elif i == possible_element:
            counter += 1
        else:
            counter -= 1

    return possible_element

if __name__ == '__main__':
    A = [2,1,2,3,4,2,1,2,2]
    N = len(A)
    print(majorityElement(A, N))
    print(majority_element(A))


