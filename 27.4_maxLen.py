"""
Given an array having both positive an negative integers. The task is to complete the function maxLen() which returns the length of maximum subarray with 0 sum. The function takes two arguments, an array A and n, where n is the size of the array A.

Input: 8    [15, -2, 2, -8, 1, 7, 10, 23]
Output: 5
"""

def maxLen(A, n):
    prefix_sum = 0
    sum_index = {}  # Stores first occurrence of prefix sums
    max_len = 0

    for i in range(n):
        prefix_sum += A[i]  # Update prefix sum
        if prefix_sum == 0:
            max_len = i + 1 # If sum is 0, entire subarray (0 to i) is valid
        
        if prefix_sum in sum_index:
            max_len = max(max_len, i - sum_index[prefix_sum])
        else:
            sum_index[prefix_sum] = i   # Store first occurrence of prefix_sum

    return max_len

A = [15, -2, 2, -8, 1, 7, 10, 23]
n = len(A)
print(maxLen(A, n))
