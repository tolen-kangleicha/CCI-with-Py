"""
Given two arrays A and B of positive integers. Your task is to find numbers which are present in the first array, but not present in the second array.
"""
def diff(A, B):
    print(A)
    print(B)
    for x in A:
        if x not in B:
            print(x, end=" ")

A = [1, 2, 3, 4, 5, 10]
B = [2, 3, 1, 0, 5]
diff(A, B)
