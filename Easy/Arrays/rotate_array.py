# Given an unsorted array of size N, 
# rotate it by D elements in the counter-clockwise direction

"""
Example 1
Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.

Example 2
Input:
N = 10, D = 3
arr[] = {2,4,6,8,10,12,14,16,18,20}
Output: 8 10 12 14 16 18 20 2 4 6
Explanation: 2 4 6 8 10 12 14 16 18 20 
when rotated by 3 elements, it becomes 
8 10 12 14 16 18 20 2 4 6.
"""

def rotate(A, D, N):
    if N < 2:
        return A
    if D > N:
        return None
    arr_start = A[0:D]
    arr_end = A[D:]
    return arr_end + arr_start


if __name__ == '__main__':
    A = [2,4,6,8,10,12,14,16,18,20]
    D = len(A)
    N = len(A)
    print(rotate(A, D, N))