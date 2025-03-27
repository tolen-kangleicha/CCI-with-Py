"""
Given two arrays A and B. Given Q queries each having a positive integer i denoting an index of the array A. 
For each query, you task is to find all the elements less than or equal to A[i] in the array B.
"""

def display(A, B, i):
    return sum(1 for x in B if x <= A[i])

print(display([1, 2, 3, 4, 7,9], [0, 1, 2, 1, 1, 4], 2))

