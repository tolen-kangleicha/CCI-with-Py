"""
Given an array which contains all elements occuring k times, but one occurs only once.
Find that unique element.
"""

from collections import Counter

def find_unique(A):
    freq = Counter(A)
    for num, count in freq.items():
        if count == 1:
            return num
    return None

print(find_unique([2, 3, 2]))
