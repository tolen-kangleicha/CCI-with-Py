"""
Given an array A[] of integers, sort the array according to frequency of elements. That is elements that have higher frequency come first.
If frequencies of two elements are same, then the smaller number comes first.
"""

from collections import Counter

def sort_by_freq(arr):
    arr.sort()
    freq = Counter(arr)
    sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
    return sorted_arr

print(sort_by_freq([4,2, 2, 2, 3, 4, 4]))
